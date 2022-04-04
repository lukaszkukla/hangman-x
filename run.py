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

words = SHEET.worksheet('words')

data = words.get_all_values()

class bcolors:
    RED = '\033[91m'
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'    
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

menu_options = True
while menu_options:
    print(' Press ' + bcolors.GREEN + '1' + bcolors.WHITE +
           ' to play game\n'
          ' Press ' + bcolors.YELLOW + '2' + bcolors.WHITE +
           ' to set difficulty\n'
          ' Press ' + bcolors.WHITE + '3' + bcolors.WHITE +
          ' to view rules\n'
          ' Press ' + bcolors.UNDERLINE + '4' + bcolors.WHITE +
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



