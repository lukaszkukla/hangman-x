from src.api import call_get_word

def display_word():
    word = call_get_word()    
    hidden_word = '_ ' * len(word)
    print(hidden_word)

def start_game():
    print('starting the game...')

def hall_of_fame():
    print('hall of fame')