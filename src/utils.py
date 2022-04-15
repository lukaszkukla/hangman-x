import os
from src.colors import Colors


def pause():
    print('\n')
    input(f'Press {Colors.VIOLET}ENTER{Colors.WHITE} to continue...')


def clear_terminal():
    """
    Clears terminal for various OS'es
    """
    os.system('clear')
