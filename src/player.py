def create_player():
    player_name = ''
    game_results[player_name] = 0



    while True:
        player_name = input('please enter your name: ').upper()
        if(player_name == '' or not player_name.isalpha() or len(player_name) < 3):
            print('name must be letter only of minimum length of 3 characters')
        else:
            
        
    return player_name, game_results[player_name]

            
    
