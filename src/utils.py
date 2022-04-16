import os
from src.colors import Colors


def pause():
    '''
    Pause and wait for user input to advance further.
    '''
    print('\n')
    input(f'Press {Colors.VIOLET}ENTER{Colors.WHITE} to continue...')


def clear_terminal():
    """
    Clear terminal for various OS'es
    """
    cmd = 'clear'
    if os.name in ('dos', 'nt'):
        cmd = 'cls'
    os.system(cmd)
