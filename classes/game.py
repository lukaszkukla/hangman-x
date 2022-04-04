from classes.colors import Colors

def how_to_play():
    print(Colors.BOLD + 'A brief history...\n' + Colors.WHITE +
    'Hangman is a digital version of the popular\n'
    'pen and paper game of unknown origin.\n\n'
    + Colors.BOLD + 'About this variation...\n' + Colors.WHITE +
    'HANGMAN-X is its variation which hints the player with the word\n'
    'category and allows it to choose between three difficulty levels.\n\n'
    + Colors.BOLD + 'Basic rules...\n' + Colors.WHITE +
    'In HANGMAN-X player is presented with the secret word to be guessed.\n'
    'In order to win the game player must type in the letter and press\n'
    'ENTER KEY to see if it is in the secret word. Upon successful guess\n'
    'of the secret word player has the option to continue the game and advance\n'
    'to the next secret word or resign. If player choose to resign and it\n'
    'accumulated enough points it will be able to add its name to the hall of fame.\n'
    'Only best players will have the privilege to add their name to the hall of fame.\n'
    'On the other hand each missed letter cost the player' + Colors.BOLD + ' 1 life.\n' 
    + Colors.WHITE + 'Each unseccessful guess adds a new body part to the gallow.\n'
    'After 6 unsuccessfull guesses player will be hanged and game will be over.\n\n'
    + Colors.BOLD + 'You have 6 lives,' + Colors.WHITE + ' can you beat the game and add your name to the' 
    + Colors.BOLD + ' HALL OF FAME?\n\n' + Colors.WHITE +
    
    'Press any key to go back to main menu...'
    )