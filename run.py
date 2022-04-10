import gspread
from google.oauth2.service_account import Credentials
from src.menu import welcome_screen

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

def main():
    """
    Run all program functions
    """
    welcome_screen()
    
main()