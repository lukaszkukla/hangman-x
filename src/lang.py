from src.colors import Colors
from src.headers import game_header
from src.utils import clear_terminal
def language():
    clear_terminal()
    game_header()
    print('\nChoose game language:\n')
    print(f'Press {Colors.BLUE}E{Colors.WHITE} ', end='')
    print(f'for {Colors.GREEN}English{Colors.WHITE}\n')
    print(f'Press {Colors.BLUE}I{Colors.WHITE} ', end='')
    print(f'for {Colors.GREEN}Italian{Colors.WHITE}')
    menu_options = True    
    while menu_options:
        option = input().upper() or 'E'
        if option == 'E':
            menu_options = False
            language = 'en'
        elif option == 'I':
            menu_options = False
            language = 'it'       
        else:
            print(f'you have entered incorrect value: {option}, please choose correct option')
        
    return language
