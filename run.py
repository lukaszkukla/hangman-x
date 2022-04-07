import gspread
import random
from classes.colors import Colors
from classes.game import *
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

data = SHEET.worksheet('words')

# words = words_bank.get_all_values()
# words = {'cars': 'Aaglander', 'animals': 'aardvark', 'cats' : 'Abyssinnian'}
# list_of_dicts = data.get_all_records()

categories = data.col_values(1)
words_bank = data.col_values(2)
data_dict = {}

# def get_words():
#     """
#     Pulls data from google sheet and creates dictionary
#     """    
#     for category, word in zip(categories, words_bank):
#             data_dict[category] = word
#     return data_dict

def get_words_based_on_level(option):
    """
    Create words bank based on difficulty level chosen by user
    """
    word_bank = []    
    if option == 'E':
        for word in words_bank:
            if len(word) < 6:
                word_bank.append(word)
    elif option == 'M':
        for word in words_bank:
            if(len(word) > 5) and (len(word) < 10):
                word_bank.append(word)
    elif option == 'H':
        for word in words_bank:
            if len(word) > 9:
                word_bank.append(word)
    return word_bank

# category = '' 
# secret_word = ''

def get_random_word(word_bank):
    """
    Pulls random category with the corresponding word from data_dict
    """        
    print('prints random word with category')
    word = random.choice(word_bank)
    print(word)
    return word

    # category = random.choice(list(data_dict.keys()))
    # random_category = category.upper()
    # secret_word = data_dict[category].upper()
    
    # print(random_category, secret_word) 

# get_random_word()

def difficulty_level():
    """
    Creates dictionary of words and categories based on users choice
    of difficulty level:
    easy: <= 5 letters
    medium: 6 - 9 letters
    hard: > 9
    """
    clear_terminal()
    print('Choose difficulty level\n'
            'Press ' + Colors.GREEN + 'E' + Colors.WHITE +
            ' for' + Colors.GREEN + ' easy\n' + Colors.WHITE +
            'Press ' + Colors.BLUE + 'M' + Colors.WHITE +
            ' for' + Colors.BLUE + ' medium\n' + Colors.WHITE +
            'Press ' + Colors.RED + 'H' + Colors.WHITE +
            ' for' + Colors.RED + ' hard\n'+ Colors.WHITE)
    difficulty_level = True
    while difficulty_level:
        option = input().upper()
        if option == 'E':
            print('easy level...')
            start_game()
            display_word()
        elif option == 'M':
            print('medium level...')
            start_game()
            display_word()
        elif option == 'H':
            print('hard level...')
            start_game()
            display_word()
        else:
            print('Not valid menu option, please try again.\n')

    return option


def display_word():    
    hidden_word = '_ ' * len(word)
    print(hidden_word)

def start_game():
    print('starting the game...')

def hall_of_fame():
    print('hall of fame')



def welcome_screen():
    """
    Displays game title, and choice of menu options
    """
    title()
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
            difficulty_level()
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