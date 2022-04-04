import gspread
from classes.colors import Colors
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

def start_game():
    print('starting the game...')

def how_to_play():
    print('game rules')

def hall_of_fame():
    print('hall of fame')

def welcome_screen():
    """
    Displays gamve title, and menu options
    """
    menu_options = True
    while menu_options:
        print('Press ' + Colors.GREEN + '1' + Colors.WHITE +
            ' to play game\n'
            'Press ' + Colors.YELLOW + '2' + Colors.WHITE +
            ' to set difficulty\n'
            'Press ' + Colors.WHITE + '3' + Colors.WHITE +
            ' to view rules\n'
            'Press ' + Colors.UNDERLINE + '4' + Colors.WHITE +
            ' to quit\n')  
        option = input().upper()
        if option == '1':
            options_menu = False
            start_game()
        elif option == '2':
            options_menu = False
            how_to_play()
        elif option == '3':
            options_menu = False
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
