from src.colors import Colors
from src.headers import hall_of_fame_header, game_header
from src.utils import clear_terminal, pause
from src.menu import welcome_screen

def hall_of_fame_scores():
    clear_terminal()
    game_header()
    hall_of_fame_header()
    ordered_scores = (dict(sorted(scores[0].items(),
                      key=operator.itemgetter(1), reverse=True)[:10]))
    for key, val in ordered_scores.items():
        print(f'{Colors.GREEN}{key}{Colors.WHITE} : {Colors.YELLOW}{val}{Colors.WHITE}')
    pause()
    welcome_screen()