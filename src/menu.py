import os
from src.colors import Colors
from src.utils import print_title, clear_terminal
from src.api import call_get_word
from src.game import display_word, hall_of_fame, start_game
from src.gallows import display_hangman

word = display_word()
width = os.get_terminal_size().columns
print(word)
def pause():
    input("Press Enter to continue...")

# use f string and many print statements to make it easer to read
def how_to_play():
    print_title()
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
    print_title()
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
            hall_of_fame()
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
    game_over = False
    guesses = []
    tries = 6 
    clear_terminal()
    print(word)
    print_title()
    print(f'Number of tries left: {tries}')
    print(f'The hidden word is: {hidden_word}')
    print(f'{display_hangman(tries)}')

    while not game_over and tries > 0:
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
                if(guess_letter in guesses):
                    raise ValueError(
                        f'you have already tried to guess letter {guess_letter}'
                    )
                elif(guess_letter not in word):
                    print(f'{guess_letter} is not in the word', end='')
                    print(f' you lost {Colors.RED}1 life{Colors.WHITE}')

                    guesses.append(guess_letter)
                    tries -= 1
                else:
                    print(word)
                    print(f'{Colors.GREEN}well done!{Colors.WHITE} {guess_letter} is in the word')

                    guesses.append(guess_letter)
                    reveal_word = list(hidden_word)
                    
                    # This code snippet is from stackoverflow.
                    indices = [i for i, letter in enumerate(word) if letter == guess_letter]
                    for index in indices:
                        reveal_word[index] = guess_letter
                        hidden_word = ''.join(reveal_word)
                    if '_' not in hidden_word:
                        game_over = True
        except ValueError as err:
            print(f'{Colors.YELLOW}{err}. Please try again.{Colors.WHITE}')
            continue

        print(display_hangman(tries))

        if(tries > 0):
            print(f'you have {tries} left')
            print(f'{guesses}')
            print(f'The hidden word is: {hidden_word}')
            print(f'Letters guessed: {sorted(guesses)}')
        elif(tries == 0):
            clear_terminal()
            print(f'you have {tries} left')
            print(f'you have been hanged!'.center(width))
            restart()
        
    if game_over:
        print(f"Congrats you have guessed the hidden word {word} !!\n".center(width))
        restart()
    else:             
        print(f'you have {tries} left')
        print(f'you have been hanged!'.center(width))
        restart()

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