import os
import gspread
import operator
from src.colors import Colors
from google.oauth2.service_account import Credentials
from src.gallows import hall_of_fame_title, game_title


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
width = os.get_terminal_size().columns


def pause():
    input("Press Enter to continue...")

def clear_terminal():
    """
    Clears terminal for various OS'es
    """
    os.system('clear')

def hall_of_fame_scores():
    clear_terminal()
    game_title()
    hall_of_fame_title()
    ordered_scores = (dict(sorted(scores[0].items(),
                      key=operator.itemgetter(1), reverse=True)[:10]))
    for key, val in ordered_scores.items():
        print(f'{Colors.GREEN}{key}{Colors.WHITE} : {Colors.YELLOW}{val}{Colors.WHITE}'.center(width))
    pause()
    clear_terminal()

    