from src.game_map.map import GameMap
from src.game_tree.tree import Tree
from src.game_tree.alphabeta import AlphaBeta


DEPTH = 3  # should always be odd so that we are maximizing us in the leaves

# Reading of data GameMap
# Sending data to server Player
def play_game(server):
    game_map: GameMap = GameMap(server.board_height, server.board_width, server.map, server.init_pos)

    while True:
        # Check if the upd is empty to make move
        update_key = server.update_board(game_map)

        if update_key == 'upd':
            game_map.display_state()

            # Tree
            data_tree = Tree()
            data_tree.create_tree(game_map, depth=DEPTH)
            data_tree.print_tree()

            # Minimax
            # minimax = MiniMax(data_tree)
            # best_move = minimax.minimax(data_tree.root)


            # Alpha-beta
            alphabeta = AlphaBeta(data_tree)
            best_move = alphabeta.alpha_beta_search(data_tree.root)

            # current position, and best move
            current_pos, current_nb = game_map.get_biggest_position()
            target_pos, _ = best_move.state.get_enemy_biggest_position()
            
            if type(target_pos) is int:
                target_pos, _ = best_move.state.get_biggest_position()

            # send move
            server.send_move([current_nb], list(current_pos), list(target_pos))
