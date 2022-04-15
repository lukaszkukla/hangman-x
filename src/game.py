import os
import operator
import gspread
from src.colors import Colors
from src.utils import clear_terminal, pause
from src.api import get_word
from src.gallows import display_hangman
from src.headers import (
    game_header,
    rules_header,
    player_wins_header,
    hall_of_fame_header,
    game_over_header)
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
word = get_word().upper()
player_score = {}


def hall_of_fame_scores():
    scores = high_scores.get_all_records()
    clear_terminal()
    game_header()
    hall_of_fame_header()
    ordered_scores = (dict(sorted(scores[0].items(),
                      key=operator.itemgetter(1), reverse=True)[:10]))
    for key, val in ordered_scores.items():
        print(f'{Colors.GREEN}{key}{Colors.WHITE}:', end='')
        print(f' {Colors.YELLOW}{val}{Colors.WHITE}')
    pause()
    game_menu()


# This code snippet is from stackoverflow
def update_highscores():
    '''
    Push user name final score to google sheet
    '''
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_results = [{'range': 'A1:ZZZ1', 'values': [keys]},
                      {'range': 'A2:ZZZ2', 'values': [values]}]
    high_scores.batch_update(update_results)


def player_name():
    '''
    Creates user, resets game score and starts game
    '''
    clear_terminal()
    global player
    while True:
        player = input('please enter a your name: ').upper()
        if player.isalpha():
            player_score[player] = 0
            start_game(word)
        else:
            print("{:^74}".format("please use letters only"))


def how_to_play():
    '''
    Displays game rules and waits for user's response
    '''
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
to the next secret word or stop the game.''')
    print(f'Player may choose to resign at any stage of the game ', end='')
    print(f'by typing word {Colors.VIOLET}resign{Colors.WHITE}.')
    print('If player accumulated enough points it will be able ', end='')
    print('to add its name to the hall of fame.')
    print('Only best players will have the privilege ', end='')
    print('to add their name to the hall of fame.')
    print(f'Every {Colors.GREEN}successful guess adds 1 point ', end='')
    print(f'{Colors.WHITE}to the final score.')
    print('On the other hand, every ', end='')
    print(f'{Colors.RED}missed letter cost the player ', end='')
    print(f'1 life and 1 point.{Colors.WHITE}')
    print('Each unseccessful try adds a new body part to the gallows.')
    print('After 6 unsuccessfull guesses player ', end='')
    print('will be hanged and game will be over.\n')
    print(f'{Colors.GREEN}You have 6 lives,{Colors.WHITE}', end='')
    print('to beat the game and add your name to the ', end='')
    print(f'{Colors.YELLOW}HALL OF FAME!{Colors.WHITE}')
    pause()
    clear_terminal()
    game_menu()


def game_menu():
    """
    Displays game header, and choice of menu options
    """
    clear_terminal()
    game_header()
    menu_options = True
    while menu_options:
        print(f'Press {Colors.BLUE}1{Colors.WHITE} ', end='')
        print(f'to {Colors.GREEN}Start Game{Colors.WHITE}')
        print(f'Press {Colors.BLUE}2{Colors.WHITE} ', end='')
        print(f'to {Colors.VIOLET}View Game Rules{Colors.WHITE}')
        print(f'Press {Colors.BLUE}3{Colors.WHITE} ', end='')
        print(f'to view {Colors.YELLOW}Hall of Fame{Colors.WHITE}')
        print(f'Press {Colors.BLUE}4{Colors.WHITE}', end='')
        print(f'to {Colors.RED}quit the game{Colors.WHITE}')
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
    Sets initial number of tries, displays empty gallows and shows the word to be guessed.
    Awaits for and validates user input and displays appropriate message.
    Adds 1 point if letter in word or subtracts 1 point and 1 life if letter not in the word.
    Displays list of guessed letters.
    Calls other functions to display headers or clear terminal.
    '''
    word = get_word().upper()
    hidden_word = '_' * len(word)
    guessed = False
    letter_guess = []
    tries = 6
    clear_terminal()
    game_header()
    print(f'number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')
    print(f'your current score is {Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
    print(f'the hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')
    print(f'{display_hangman(tries)}')

    while not guessed and tries > 0:
        guess_letter = input('guess the letter:\n').upper()
        try:
            if(guess_letter == 'RESIGN'):
                clear_terminal()
                guessed = False
                tries = 0
            elif(guess_letter == 'CHEAT'):
                print(word)
                continue
            elif(len(guess_letter) > 1):
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
                    player_score[player] -= 1
                    print(f'your current score is {Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
                else:
                    clear_terminal()
                    game_header()
                    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')

                    player_score[player] += 1
                    print(player_score[player])
                    print(f'your current score is {Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
                    
                    print(f'{Colors.GREEN}well done!{Colors.WHITE} {guess_letter} is in the word')
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
            print(player_score[player])
            print(f'you have {Colors.BLUE}{tries}{Colors.WHITE} tries left')
            print(f'the hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}')
            print(f'letters guessed: {Colors.BOLD}{str(sorted(letter_guess))}{Colors.WHITE}')

    if guessed:
        clear_terminal()
        player_wins_header()
        print(f'congrats!, you guessed the word: {Colors.VIOLET}{word}{Colors.WHITE} correctly!')
        
        while True:            
            play_again_after_win = input('  ' * 10 +
                                         ' play again? ( y / n ) : ').upper()
            if(play_again_after_win == 'Y'):
                player_score[player] += 10
                word = get_word().upper()
                start_game(word)                
            elif(play_again_after_win == 'N'):
                player_score[player] += 10                
                if(player not in scores[0].keys()):
                    scores[0][player] = player_score[player]
                    game_header()
                    game_over_header()
                    print(f'{Colors.CYAN}{player}{Colors.WHITE} your final score is {Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
                    pause()
                    update_highscores()
                    clear_terminal()
                    hall_of_fame_header()
                    hall_of_fame_scores()
                elif(player_score[player] > scores[0][player]):
                    scores[0][player] = player_score[player]
                    update_highscores()
                    clear_terminal()
                    hall_of_fame_header()
                    hall_of_fame_scores()
                else:
                    game_menu()
    else:
        clear_terminal()
        game_header()
        game_over_header()        
        print(f'you have been hanged!')
        print(display_hangman(tries))        
        print(f'the hidden word was: {Colors.YELLOW}{word.upper()}{Colors.WHITE}\n')
        print(f'{Colors.CYAN}{player}{Colors.WHITE} your final score is {Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
        pause()
        if(player not in scores[0].keys()):
            scores[0][player] = player_score[player]
            update_highscores()
            clear_terminal()
            hall_of_fame_header()
            hall_of_fame_scores()
        elif(player_score[player] > scores[0][player]):
            scores[0][player] = player_score[player]
            update_highscores()
            clear_terminal()
            hall_of_fame_header()
            hall_of_fame_scores()
        else:
            game_menu()

        while True:
            play_again_after_lose = input(f'play again? ( y / n ) : ').upper()
            if(play_again_after_lose == 'Y'):
                word = get_word().upper()
                start_game(word)
            elif(play_again_after_lose == 'N'):
                word = get_word().upper()
                game_menu()
            else:
                print(f'please choose option y or n')