from src.colors import Colors
from src.utils import print_title, clear_terminal
from src.api import call_get_word
from src.game import display_word, hall_of_fame

def pause():
    input("Press Enter to continue...")

# use f string and many print statements to make it easer to read
def how_to_play():
    print_title()
    print(Colors.BOLD + 'A brief history...' + Colors.WHITE)
    print('Hangman is a digital version of the popular\n'
    'pen and paper game of unknown origin.\n\n'
    + Colors.BOLD + 'About this variation...' + Colors.WHITE)
    print('HANGMAN-X is its variation which hints the player with the word\n'
    'category and allows it to choose between three difficulty levels.\n\n'
    + Colors.BOLD + 'Basic rules...' + Colors.WHITE)
    print('In HANGMAN-X player is presented with the secret word to be guessed.\n'
    'In order to win the game player must type in the letter and press\n'
    'ENTER KEY to see if it is in the secret word. Upon successful guess\n'
    'of the secret word player has the option to continue the game and advance\n'
    'to the next secret word or resign. If player choose to resign and it\n'
    'accumulated enough points it will be able to add its name to the hall of fame.\n'
    'Only best players will have the privilege to add their name to the hall of fame.\n')
    print('On the other hand each' + Colors.RED + ' missed letter cost the player 1 life.\n' 
    + Colors.WHITE + 'Each unseccessful guess adds a new body part to the gallow.\n'
    'After 6 unsuccessfull guesses player will be hanged and game will be over.\n\n'
    + Colors.GREEN + 'You have 6 lives,' + Colors.WHITE + ' to beat the game and add your name to the' 
    + Colors.YELLOW + ' HALL OF FAME\n\n' + Colors.WHITE
    )
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
            display_word()
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