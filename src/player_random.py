import random
from src.game_map.map import GameMap

DEPTH = 3  # should always be odd so that we are maximizing us in the leaves

# Reading of data GameMap
# Sending data to server Player
def play_game(server):
    iterations = 1
    game_map: GameMap = GameMap(server.board_height, server.board_width, server.map, server.init_pos)
    while True:
        update_key = server.update_board(game_map)
        if update_key == 'upd':
            # current position, and best move
            current_pos, current_nb = game_map.get_biggest_position()
            
            moves = game_map.possible_moves()
            
            # send move
            server.send_move([current_nb], list(current_pos), list(random.choice(moves)))
            iterations += 1