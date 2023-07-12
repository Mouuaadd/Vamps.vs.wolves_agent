from src.game_map.map import GameMap
import random



def calculate_utility_value(map: GameMap):
    our_pos, our_units = map.get_biggest_position()
    enemy_pos, enemy_units = map.get_enemy_biggest_position()

    diff_coef = 10
    kill_coef = 100
    max_eat_coef = 1

    if type(our_pos) is int:
        return -100000

    if type(enemy_pos) is int:
        return 100000

    

    our_max_eat = max_eat(our_pos,our_units,map.humans_state, proximity=max(map.get_grid_size()))
    enemy_max_eat = max_eat(enemy_pos,enemy_units,map.humans_state, proximity=max(map.get_grid_size()))
    our_max_kill = max_kill(our_pos,our_units,map.get_enemy_dict(), proximity=max(map.get_grid_size()))
    # enemy_max_kill = max_kill(our_pos,our_units,map.get_biggest_position(), proximity=max(map.get_grid_size()))

    unit_diff = diff_coef*(our_units-enemy_units)
    kill = kill_coef*our_max_kill
    max_eat_diff = max_eat_coef*(our_max_eat - enemy_max_eat)
    return unit_diff + max_eat_diff + kill + random.uniform(0,0.01)


def max_eat(position, number, humans_states, proximity=6):
    max_eat = 0
    x, y = position

    for i in range(- proximity, proximity + 1):
        for j in range(- proximity, proximity + 1):
            if (x + i, y + j) in humans_states.keys():
                if humans_states[x + i, y + j] <= number:
                    if humans_states[x + i, y + j]/max(abs(i),abs(j)) > max_eat:
                        max_eat = humans_states[x + i, y + j]/max(abs(i),abs(j))
    return max_eat

def max_kill(position, number, enemy_dict, proximity=6):
    x, y = position
    max_kill = 0
    for i in range(- proximity, proximity + 1):
        for j in range(- proximity, proximity + 1):
            if (x + i, y + j) in enemy_dict.keys():
                if enemy_dict[x + i, y + j] < number:
                    if enemy_dict[x + i, y + j]/max(abs(i),abs(j)) > max_kill:
                        max_kill = enemy_dict[x + i, y + j]/max(abs(i),abs(j))
    return max_kill


#Counting humans in range

# def humans_in_proximity(position,humans_states,proximity=1):
#     count = 0
#     for i in range(-proximity,proximity+1):
#         for j in range(-proximity, proximity+1):
#             if (position[0]+i,position[1]+j) in humans_states.keys():
#                 count += 1
#     print(f"found {count} humans")
#     return count




