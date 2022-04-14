import os
from src.colors import Colors
from src.utils import clear_terminal, pause, hall_of_fame_scores
from src.api import call_get_word
from src.game import display_word, hall_of_fame
from src.gallows import game_title, rules_title, player_wins_title, display_hangman, hall_of_fame_title

import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-x')
high_scores = SHEET.worksheet('highscores')
scores = high_scores.get_all_records()

word = call_get_word().upper()
width = os.get_terminal_size().columns
game_results = {}
score = 0
print(word)


def update_highscores():
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_results = [{'range': 'A1:Z1', 'values': [keys]},
                      {'range': 'A2:Z2', 'values': [values]}]
    high_scores.batch_update(update_results)

# use f string and many print statements to make it easer to read
def how_to_play():
    game_title()
    rules_title()
    print(f'{Colors.BOLD}A brief history...{Colors.WHITE}')
    print(f'''Hangman is a digital version of the popular
pen and paper game of unknown origin.\n''')
    print(f'{Colors.BOLD}About this variation...{Colors.WHITE}')
    print(f'''HANGMAN-X is its variation which allows player to choose
between three difficulty levels.\n''')
    print(f'{Colors.BOLD}Basic rules...{Colors.WHITE}')
    print(f'''In HANGMAN-X player is presented with the secret word to be guessed.
In order to win the game player must type in the letter and press
ENTER KEY to see if it is in the secret word. Upon successful guess
of the secret word player has the option to continue the game and advance
to the next secret word or resign. If player choose to resign and it
accumulated enough points it will be able to add its name to the hall of fame.
Only best players will have the privilege to add their name to the hall of fame.''')
    print(f'''On the other hand each {Colors.RED}missed letter cost the player 1 life. 
{Colors.WHITE}Each unseccessful try adds a new body part to the gallows.
After 6 unsuccessfull guesses player will be hanged and game will be over.\n''')
    print(f'{Colors.GREEN}You have 6 lives,{Colors.WHITE} to beat the game', end='')
    print(f' and add your name to the {Colors.YELLOW}HALL OF FAME!\n\n{Colors.WHITE}')
    pause()
    clear_terminal()
    welcome_screen()


def welcome_screen():
    """
    Displays game title, and choice of menu options
    """
    clear_terminal()
    game_title()
    menu_options = True
    while menu_options:
        print('Press ' + Colors.BLUE + '1' + Colors.WHITE +
            ' to start game\n'
            'Press ' + Colors.BLUE + '2' + Colors.WHITE +
            ' to view rules\n'
            'Press ' + Colors.BLUE + '3' + Colors.WHITE +
            ' to view hall of fame\n'
            'Press ' + Colors.BLUE + '4' + Colors.WHITE +
            ' to quit\n')  
        option = input().upper()
        if option == '1':
            menu_options = False
            start_game(word)
        elif option == '2':
            menu_options = False
            clear_terminal()
            how_to_play()
        elif option == '3':
            menu_options = False
            clear_terminal()
            hall_of_fame_title()
            hall_of_fame_scores()
        elif option == '4':
            exit()
        else:
            print('Not valid menu option, please try again.\n')

def start_game(word):
    '''
    Starts the game.
    Sets initial tries, displays empty gallows and shows the word to be guessed.
    Calls restart game function if player runs out of tries.
    '''   
    hidden_word = '_' * len(word)
    # hidden_word = display_word().upper()
    global score
    game_over = False
    guessed = False
    letter_guess = []
    tries = 6 
    clear_terminal()
    print(word)
    game_title()
    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')
    print(f'your current score is {Colors.GREEN}{score}{Colors.WHITE}\n')
    print(f'The hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')
    print(f'{display_hangman(tries)}')

    while not guessed and tries > 0:
        guess_letter = input('Guess the letter:\n').upper()
        try:
            if(len(guess_letter) > 1):
                raise ValueError(
                    f'please enter only one character per try, you entered {len(guess_letter)} characters'
                )
            elif(not guess_letter.isalpha()):
                raise ValueError(
                    f'please enter letters only, your guess was {guess_letter}'
                )
            elif(len(guess_letter) == 1 and guess_letter.isalpha()):
                if(guess_letter in letter_guess):
                    raise ValueError(
                        f'you have already tried to guess letter {guess_letter}'
                    )
                elif(guess_letter not in word):
                    clear_terminal()
                    game_title()
                    print(f'{Colors.RED}{guess_letter}{Colors.WHITE} is not in the word', end='')
                    print(f' you lost {Colors.RED}1 life{Colors.WHITE}\n')
                    
                    letter_guess.append(guess_letter)
                    tries -= 1
                    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')

                    score -=1
                    print(f'your current score is {Colors.GREEN}{score}{Colors.WHITE}\n')

                    # print(f'The hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')

                else:
                    clear_terminal()
                    game_title()
                    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')

                    score =+ 1
                    print(f'your current score is {Colors.GREEN}{score}{Colors.WHITE}\n')
                    
                    print(f'{Colors.GREEN}well done!{Colors.WHITE} {guess_letter} is in the word')
                    print(word)
                    print('\n')

                    letter_guess.append(guess_letter)
                    reveal_word = list(hidden_word)
                    
                    # This code snippet is from stackoverflow.
                    indices = [i for i, letter in enumerate(word) if letter == guess_letter]
                    for index in indices:
                        reveal_word[index] = guess_letter
                        hidden_word = ''.join(reveal_word)
                    if '_' not in hidden_word:
                        guessed = True
        except ValueError as err:
            print(f'{Colors.YELLOW}{err}. Please try again.{Colors.WHITE}')
            continue

        print(display_hangman(tries))

        if(tries > 0):
            score +=1
            print(f'you have {Colors.BLUE}{tries}{Colors.WHITE} tries left')
            # print(f'{Colors.BOLD}{letter_guess}{Colors.WHITE}')
            print(f'The hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}')
            print(f'Letters guessed: {Colors.BOLD}{sorted(letter_guess)}{Colors.WHITE}')
        # elif(tries == 0):
        #     clear_terminal()
        #     print(f'you have {tries} left')
        #     print(f'you have been hanged!'.center(width))
        #     restart()
    
    if guessed:
        clear_terminal()
        player_wins_title()
        print(f'Congrats!, you guessed the word: {word} correctly! You Win!')
        
        while True:            
            play_again_after_win = input('  ' * 10 +
                                         ' Play Again? ( Y / N ) : ').upper()
            if(play_again_after_win == 'Y'):
                current_score = score + 10
                word = call_get_word().upper()
                # game_results[player] += 1
                start_game(word)
                
            elif(play_again_after_win == 'N'):
                score += 10
                # game_results[player] += 1
                welcome_screen()
                # if(player not in scores[0].keys()):
                #     scores[0][player] = scores[player]
                #     update_highscores_sheet()
                #     welcome_screen()
                # elif(scores[player] > scores[0][player]):
                #     scores[0][player] = scores[player]
                #     update_highscores_sheet()
                #     welcome_screen()
                # else:
                #     welcome_screen()
    else:             
        print(f'you have {tries} tries left')
        print(f'you have been hanged!'.center(width))
        print(f'the hidden word was: {word.upper()}')

        while True:
            play_again_after_lose = input(f'Play Again? ( Y / N ) : '.center(width)).upper()
            if(play_again_after_lose == 'Y'):
                start_game(call_get_word())
            elif(play_again_after_lose == 'N'):
                welcome_screen()
            else:
                print(f'Please choose option Y or N'.center(width))

def restart():
    """
    Ask the users if they want to continue or quit
    """
    while True:
        user_input = input(
            "Would you like to continue? [Y]ES/[N]O\n".center(width)).upper()
        if user_input == "Y":
            clear_terminal()
            call_get_word()
            start_game(word)
        elif user_input == "N":
            clear_terminal()
            welcome_screen()
        else:
            clear_terminal()
            print("Invalid choise, please chose again\n".center(width))  