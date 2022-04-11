from src.colors import Colors

def game_title():
    '''
    Displays game title at the top of the screen
    '''
    print(
    f'''{Colors.RED}  
         _ _   _   _  _   __  _   _   _   _  _     __ __
        | U | / \ | \| | / _|| \_/ | / \ | \| | __ \ V /
        |   || o ||  \\ |( |_n| \_/ || o || \\  ||__| ) ( 
        |_n_||_n_||_|\_| \__/|_| |_||_n_||_|\_|    /_n_\\
        {Colors.WHITE}
    '''
    )

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        '''
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / \\
                  -
               
                   __   _   _   _  ___    _   _ _  ___  ___ 
                  / _| / \ | \_/ || __|  / \ | | || __|| o \\
                 ( |_n| o || \_/ || _|  ( o )| V || _| |   /
                  \__/|_n_||_| |_||___|  \_/  \_/ |___||_|\\
                  
               ''',
        # head, torso, both arms, and one leg
        '''
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / 
                  -
               ''',
        # head, torso, and both arms
        '''
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |      
                  -
               ''',
        # head, torso, and one arm
        '''
                  --------O
                  |      |
                  |      O
                  |     \|
                  |      |
                  |     
                  -
               ''',
        # head and torso
        '''
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
               ''',
        # head
        '''
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
               ''',
        # initial empty state
        '''
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
               ''',
    ]
    return stages[tries]

def player_wins_title():
   print(
      '''
      __ __ _   _ _   _ _ _  _  _  _ 
      \ V // \ | | | | | | || || \| |
       \ /( o )| U | | V V || || \\ |
       |_| \_/ |___|  \_n_/ |_||_|\_|
         
      '''
   )

def hall_of_fame_title():
   print(
      f'''{Colors.YELLOW}
       _ _   _   _    _      _   ___   ___  _   _   _  ___ 
      | U | / \ | |  | |    / \ | __| | __|/ \ | \_/ || __|
      |   || o || |_ | |_  ( o )| _|  | _|| o || \_/ || _| 
      |_n_||_n_||___||___|  \_/ |_|   |_| |_n_||_| |_||___|
      {Colors.WHITE}    
      '''
   )

def rules_title():
   print(
      f'''{Colors.YELLOW}
                   ___  _ _  _    ___  __ 
                  | o \| | || |  | __|/ _|
                  |   /| U || |_ | _| \_ \\
                  |_| \\|___||___||___||__/
      {Colors.WHITE}    
      '''
   )