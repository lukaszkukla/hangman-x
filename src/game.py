import os
import operator
import gspread
from src.colors import Colors
from src.utils import clear_terminal, pause
from src.api import get_word
from src.gallows import display_hangman
from src.headers import (
    disclaimer_header,
    game_header,
    rules_header,
    player_wins_header,
    hall_of_fame_header,
    game_over_header,
    disclaimer_header)
from google.oauth2.service_account import Credentials
from src.lang import language


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
word = get_word(lang='en').upper()
player_score = {}


def hall_of_fame_scores():
    '''
    Get and sort data from google sheet.
    Return top 10 highscore items.
    '''
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
    Create user, let to choose languge, reset game score and start the game
    '''
    global player
    clear_terminal()
    game_header()
    while True:
        player = input('Please enter your name: ').upper()
        if player.isalpha():
            global lang
            print(f'\nWelcome {Colors.CYAN}{player}{Colors.WHITE}')
            pause()
            lang = language()
            player_score[player] = 0
            
            start_game(word)
        else:
            print(f'Please use {Colors.YELLOW}letters only{Colors.WHITE}\n')


def how_to_play():
    '''
    Display game rules and waits for user's response
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
    print(f'{Colors.GREEN}You have 6 lives {Colors.WHITE}', end='')
    print('to beat the game and add your name to the ', end='')
    print(f'{Colors.YELLOW}HALL OF FAME!{Colors.WHITE}')
    pause()
    clear_terminal()
    game_menu()


def game_menu():
    """
    Display game header, and choice of menu options
    """
    clear_terminal()
    game_header()
    menu_options = True
    while menu_options:
        print(f'Press {Colors.BLUE}1{Colors.WHITE} ', end='')
        print(f'to {Colors.GREEN}Start Game{Colors.WHITE}')
        print(f'Press {Colors.BLUE}2{Colors.WHITE} ', end='')
        print(f'to view {Colors.VIOLET}Game Rules{Colors.WHITE}')
        print(f'Press {Colors.BLUE}3{Colors.WHITE} ', end='')
        print(f'to view {Colors.YELLOW}Hall of Fame{Colors.WHITE}')
        print(f'Press {Colors.BLUE}4{Colors.WHITE} ', end='')
        print(f'to {Colors.RED}Quit game{Colors.WHITE}\n')
        print(f'Press {Colors.BLUE}5{Colors.WHITE} ', end='')
        print(f'for {Colors.UNDERLINE}Disclaimer{Colors.WHITE}\n')
        option = input('Choose one of the main menu options: ').upper()
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
            print('\nThank you for playing. I hope you enjoyed it.\n')
            print('Shutting down...\n')
            exit()
        elif option == '5':
            clear_terminal()
            game_header()
            disclaimer_header()
            print('Please note that the game functionality depends on the external link.')
            print('In case there were any changes to it please contact me via ')
            print('Code Institute so I can update the link ', end='')            
            print('to ensure the game functions properly.\n')
            print('Thank you for your understanding.')
            pause()
            game_menu()
        else:
            print(f'{option} is not a valid menu option, please try again.\n')


def start_game(word):
    '''
    Start the game.
    Set initial number of tries, display empty gallows
    and show the word to be guessed.
    Await for and validate user input.
    Display appropriate error message.
    Add 1 point if letter in word or subtract 1 point
    and 1 life if letter not in the word.
    Display list of guessed letters.
    Call other functions to display headers and clear terminal.
    Ask player to continue upon game end and validate for user input.
    Add user and display hall of fame if enough points accumulated.
    '''
    word = get_word(lang).upper()
    hidden_word = '_' * len(word)
    guessed = False
    letter_guess = []
    tries = 6
    clear_terminal()
    game_header()
    print(f"{Colors.CYAN}{player}{Colors.WHITE}'s stats\n")
    print(f'Number of tries left: {Colors.BLUE}{tries}{Colors.WHITE}\n')
    print('Your current score is : ', end='')
    print(f'{Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
    print(f'The hidden word is: {Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')
    print(f'{display_hangman(tries)}')

    while not guessed and tries > 0:
        guess_letter = input('Guess a letter:\n').upper()
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
                    f'Please enter only one character per try, you entered {len(guess_letter)} characters'
                )
            elif(not guess_letter.isalpha()):
                raise ValueError(
                    f'Please enter letters only, your guess was {guess_letter}'
                )
            elif(len(guess_letter) == 1 and guess_letter.isalpha()):
                if(guess_letter in letter_guess):
                    raise ValueError(
                        f'You already tried letter {guess_letter}'
                    )
                elif(guess_letter not in word):
                    letter_guess.append(guess_letter)
                    clear_terminal()
                    game_header()
                    print(f"{Colors.CYAN}{player}{Colors.WHITE}'s stats\n")
                    print(f'{Colors.RED}{guess_letter}{Colors.WHITE} ', end='')
                    print('is not in the word', end='')
                    print(f' you lost {Colors.RED}1 life{Colors.WHITE}\n')
                    tries -= 1
                    print('Number of tries left: ', end='')
                    print(f'{Colors.BLUE}{tries}{Colors.WHITE}\n')
                    player_score[player] -= 1
                    print(f'Current score is ', end='')
                    print(f'{Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
                    print(f'The hidden word is: ', end='')
                    print(f'{Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')
                else:
                    letter_guess.append(guess_letter)
                    reveal_word = list(hidden_word)

                    # This code snippet is from stackoverflow
                    indices = (
                        [i for i, letter in enumerate(word) if letter == guess_letter]
                        )
                    for index in indices:
                        reveal_word[index] = guess_letter
                        hidden_word = ''.join(reveal_word)
                    if '_' not in hidden_word:
                        guessed = True

                    clear_terminal()
                    game_header()
                    print(f"{Colors.CYAN}{player}{Colors.WHITE}'s stats\n")

                    print(f'{Colors.GREEN}Well done!{Colors.WHITE} ', end='')
                    print(f'{guess_letter} is in the word\n')

                    print('Number of tries left: ', end='')
                    print(f'{Colors.BLUE}{tries}{Colors.WHITE}\n')

                    player_score[player] += 1
                    print('Current score is ', end='')
                    print(f'{Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')

                    print(f'The hidden word is: ', end='')
                    print(f'{Colors.YELLOW}{hidden_word}{Colors.WHITE}\n')

        except ValueError as err:
            print(f'{Colors.YELLOW}{err}. Please try again.{Colors.WHITE}')
            continue

        print(display_hangman(tries))

        if(tries > 0):
            print(f'Letters guessed: {Colors.BOLD} ', end='')
            print(f'{str(sorted(letter_guess))}{Colors.WHITE}\n')

    if guessed:
        clear_terminal()
        player_wins_header()
        print(f'Congrats {Colors.CYAN}{player}{Colors.WHITE}! ', end='')
        print(f'You guessed the word: ', end='')
        print(f'{Colors.YELLOW}{word}{Colors.WHITE} correctly!\n')
        while True:
            play_again_after_win = input(
                'Would you like to play again? ( y / n ) : '
                ).upper()
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
                    print(f'{Colors.CYAN}{player}{Colors.WHITE} ', end='')
                    print(f'{player}, your final {Colors.GREEN}', end='')
                    print(f'score is {player_score[player]}{Colors.WHITE}\n')
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
        print(f'{Colors.CYAN}{player}{Colors.WHITE}, you have been hanged! ', end='')
        print(f'Your final score is ', end='')
        print(f'{Colors.GREEN}{player_score[player]}{Colors.WHITE}\n')
        print(display_hangman(tries))
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
