from src.game_map.map import GameMap


def new_maps(game_map: GameMap, moves):
    nodes = []
    for move in moves:
        # this needs to work for other specie too
        new_map = game_map.generate_updated_map(move)
        # new_map = game_map.generate_updated_map(initial_pos, move)
        nodes.append(new_map)
    return nodes


