# import gspread
# from google.oauth2.service_account import Credentials
# from src.utils import clear_terminal
from src.menu import welcome_screen

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('hangman-x')
# high_scores = SHEET.worksheet('highscores')
# scores = high_scores.get_all_records()

# def hall_of_fame_scores():
#     clear_terminal()
#     print("{:^70}".format("HIGH SCORES : "))
#     print("\n")
#     ordered_scores = (dict(sorted(scores[0].items(),
#                         key=operator.itemgetter(1), reverse=True)[:5]))
#     for key, val in ordered_scores.items():
#         print("{:^70}".format(f"{key} : {val}"))
#         print("\n")

def main():
    """
    Run all program functions
    """
    welcome_screen()    
    
main()