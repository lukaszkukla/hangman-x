from src.api import call_get_word
from src.utils import clear_terminal, print_title
from src.colors import Colors

def display_word():
    word = call_get_word().upper()
    return word

def start_game():
    print('starting the game...')

def hall_of_fame():
    print('hall of fame')

      
