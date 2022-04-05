import gspread
import os
import random
from classes.colors import Colors
from classes.game import how_to_play
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

words = SHEET.worksheet('words')

data = words.get_all_values()

def clear_terminal():
    """
    Clears terminal for various OS'es
    """
    cmd = 'clear'
    if os.name in ('dos', 'nt'):
        cmd = 'cls'
    os.system(cmd)

def start_game():
    print('starting the game...')

def hall_of_fame():
    print('hall of fame')

def welcome_screen():
    """
    Displays game title, and choice of menu options
    """
    print(
    """
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗     ██╗  ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║     ╚██╗██╔╝
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║█████╗╚███╔╝ 
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║╚════╝██╔██╗ 
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║     ██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═╝  ╚═╝
    """
    )
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
            clear_terminal()
            start_game()
            print(random_word())
        elif option == '2':
            menu_options = False
            how_to_play()
        elif option == '3':
            menu_options = False
            hall_of_fame()
        elif option == '4':
            exit()
        else:
            print('Not valid menu option, please try again.\n')

def main():
    """
    Run all program functions
    """
    welcome_screen()

main()