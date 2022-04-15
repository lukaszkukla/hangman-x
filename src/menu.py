import os
from src.colors import Colors
from src.utils import clear_terminal, pause
from src.api import get_word
from src.gallows import  display_hangman
from src.headers import game_header, rules_header, player_wins_header, hall_of_fame_header, game_over_header
import gspread
from google.oauth2.service_account import Credentials
import operator

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

word = get_word().upper()
width = os.get_terminal_size().columns
game_results = {}
score = 0
print(word)

# This code snippet is from stackoverflow
def update_highscores():
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_results = [{'range': 'A1:Z1', 'values': [keys]},
                      {'range': 'A2:Z2', 'values': [values]}]
    high_scores.batch_update(update_results)

def player_name():
    clear_terminal()
    global player
    while True:
        player = input('please enter a your name: ').upper()
        if player.isalpha():
            game_results[player] = 0
            start_game(word)
        else:
            print("{:^74}".format("please use letters only"))

def hall_of_fame_scores():
    clear_terminal()
    game_header()
    hall_of_fame_header()
    ordered_scores = (dict(sorted(scores[0].items(),
                      key=operator.itemgetter(1), reverse=True)[:10]))
    for key, val in ordered_scores.items():
        print(f'{Colors.GREEN}{key}{Colors.WHITE} : {Colors.YELLOW}{val}{Colors.WHITE}')
    pause()
    welcome_screen()

def how_to_play():
    game_header()
    rules_header()
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
    Displays game header, and choice of menu options
    """
    clear_terminal()
    game_header()
    menu_options = True
    while menu_options:
        print('press ' + Colors.BLUE + '1' + Colors.WHITE +
            ' to start game\n'
            'press ' + Colors.BLUE + '2' + Colors.WHITE +
            ' to view rules\n'
            'press ' + Colors.BLUE + '3' + Colors.WHITE +
            ' to view hall of fame\n'
            'press ' + Colors.BLUE + '4' + Colors.WHITE +
            ' to quit\n')  
        option = input().upper()
        if option == '1':
            menu_options = False
            player_name()
        elif option == '2':
            menu_options = False
            clear_terminal()
            how_to_play()
        elif option == '3':
            menu_options = False
            clear_terminal()
            hall_of_fame_header()
            hall_of_fame_scores()
        elif option == '4':
            exit()
        else:
            print('not a valid menu option, please try again.\n')

def start_game(word):
    '''
    Starts the game.
    Sets initial tries, displays empty gallows and shows the word to be guessed.
    Calls restart game function if player runs out of tries.
    '''
    word = get_word().upper()
    hidden_word = '_' * len(word)
    global score
    game_over = False
    guessed = False
    letter_guess = []
    tries = 6 
    clear_terminal()
    print(word)
    game_header()
    print(f'number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')
    print(f'your current score is {Colors.GREEN}{game_results[player]}{Colors.WHITE}\n')
    print(f'the hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')
    print(f'{display_hangman(tries)}')

    while not guessed and tries > 0:
        guess_letter = input('guess the letter:\n').upper()
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
                    game_header()
                    print(f'{Colors.RED}{guess_letter}{Colors.WHITE} is not in the word', end='')
                    print(f' you lost {Colors.RED}1 life{Colors.WHITE}\n')
                    
                    letter_guess.append(guess_letter)
                    tries -= 1
                    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')

                    game_results[player] -=1
                    print(f'your current score is {Colors.GREEN}{game_results[player]}{Colors.WHITE}\n')

                else:
                    clear_terminal()
                    game_header()
                    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')

                    game_results[player] += 1
                    print(game_results[player])
                    print(f'your current score is {Colors.GREEN}{game_results[player]}{Colors.WHITE}\n')
                    
                    print(f'{Colors.GREEN}well done!{Colors.WHITE} {guess_letter} is in the word')
                    print(word)
                    print('\n')

                    letter_guess.append(guess_letter)
                    reveal_word = list(hidden_word)
                    
                    # This code snippet is from stackoverflow
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
            print(game_results[player])
            print(f'you have {Colors.BLUE}{tries}{Colors.WHITE} tries left')
            print(f'the hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}')
            print(f'letters guessed: {Colors.BOLD}{str(sorted(letter_guess))}{Colors.WHITE}')
        # elif(tries == 0):
        #     clear_terminal()
        #     print(f'you have {tries} left')
        #     print(f'you have been hanged!')
        #     restart()
    
    if guessed:
        clear_terminal()
        player_wins_header()
        print(f'congrats!, you guessed the word: {Colors.VIOLET}{word}{Colors.WHITE} correctly!')
        
        while True:            
            play_again_after_win = input('  ' * 10 +
                                         ' play again? ( y / n ) : ').upper()
            if(play_again_after_win == 'Y'):
                game_results[player] += 10
                word = get_word().upper()
                start_game(word)                
            elif(play_again_after_win == 'N'):
                game_results[player] += 10                
                if(player not in scores[0].keys()):
                    scores[0][player] = game_results[player]
                    update_highscores()
                    clear_terminal()
                    hall_of_fame_header()
                    print('congrats you are in the hall of fame')
                    hall_of_fame_scores()
                elif(game_results[player] > scores[0][player]):
                    scores[0][player] = game_results[player]
                    update_highscores()
                    clear_terminal()
                    hall_of_fame_header()
                    hall_of_fame_scores()
                else:
                    welcome_screen()
    else:
        print(f'you have been hanged!')
        game_over_header()
        print(f'the hidden word was: {Colors.YELLOW}{word.upper()}{Colors.WHITE}')

        while True:
            play_again_after_lose = input(f'play again? ( y / n ) : ').upper()
            if(play_again_after_lose == 'Y'):
                word = get_word().upper()
                start_game(word)
            elif(play_again_after_lose == 'N'):
                word = get_word().upper()
                welcome_screen()
            else:
                print(f'please choose option y or n')

# def restart():
#     """
#     Ask the users if they want to continue or quit
#     """
#     while True:
#         user_input = input(
#             'would you like to continue? ( y / n ) : \n')
#         if user_input == "Y":
#             clear_terminal()
#             get_word()
#             start_game(get_word)
#         elif user_input == "N":
#             clear_terminal()
#             welcome_screen()
#         else:
#             clear_terminal()
#             print('invalid choise, please chose again\n')  