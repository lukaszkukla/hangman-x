from src.colors import Colors

def game_header():
   '''
   Displays game title
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

def player_wins_header():
   '''
   Displays you win header
   '''
   print(
      f'''{Colors.GREEN}
     __ __ _   _ _   _ _ _  _  _  _ 
     \ V // \ | | | | | | || || \| |
      \ /( o )| U | | V V || || \\ |
      |_| \_/ |___|  \_n_/ |_||_|\_|
      {Colors.WHITE}   
      '''
   )

def hall_of_fame_header():
   '''
   Displays hall of fame header
   '''
   print(
      f'''{Colors.YELLOW}
     _ _   _   _    _      _   ___   ___  _   _   _  ___ 
    | U | / \ | |  | |    / \ | __| | __|/ \ | \_/ || __|
    |   || o || |_ | |_  ( o )| _|  | _|| o || \_/ || _| 
    |_n_||_n_||___||___|  \_/ |_|   |_| |_n_||_| |_||___|
      {Colors.WHITE}    
      '''
   )

def rules_header():
   '''
   Displays game rules header
   '''
   print(
      f'''{Colors.YELLOW}
     ___  _ _  _    ___  __ 
    | o \| | || |  | __|/ _|
    |   /| U || |_ | _| \_ \\
    |_| \\|___||___||___||__/
      {Colors.WHITE}    
      '''
   )

def game_over_header():
   '''
   Displays game over header
   '''
   print(
      f'''{Colors.RED}  
      __   _   _   _  ___    _   _ _  ___  ___ 
     / _| / \ | \_/ || __|  / \ | | || __|| o \\
    ( |_n| o || \_/ || _|  ( o )| V || _| |   /
     \__/|_n_||_| |_||___|  \_/  \_/ |___||_|\\
        {Colors.WHITE}
    '''
    )
