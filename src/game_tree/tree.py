from src.game_map.map import GameMap
from src.game_tree.utils import new_maps
from src.game_tree.heuristics import calculate_utility_value


class Node:
    def __init__(self, state, value=- float('inf'), parent=None):
        self.state: GameMap = state
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, map: GameMap, depth):
        self.root = Node(map)

        if not bool(self.root.state.vamps_state) or not bool(self.root.state.wolves_state):
            self.root = calculate_utility_value(self.root.state)
            return
        else:
            find_children(map, self.root)

            self.build_tree(self.root, depth-1)

    def build_tree(self, parent: Node, depth):
        if depth < 1:
            for child in parent.children:
                child.value = calculate_utility_value(child.state)
            return

        for child in parent.children:
            if not bool(child.state.vamps_state) or not bool(child.state.wolves_state):
                child.value = calculate_utility_value(child.state)
                return
            else:
                child.value = None
                child.state.is_vampire = not child.state.is_vampire

                find_children(child.state, child)
                self.build_tree(child, depth - 1)

    def print_tree(self, node=None, level=0):
        leaf = '    ' * (level - 1) + '└── ' * (level > 0)
        not_leaf = '    ' * level + '└── '

        if node is None:
            node = self.root

        if isinstance(node, Node):
            if not bool(node.children):
                print(not_leaf + "Utility Value = {}\t Type = {}\t CUR POS: {} \t\t({})".format(node.value, node.state.is_vampire, node.state.get_current_pos()[0], level))
            else:
                print(leaf + "Utility Value = {}\t Type = {}\t CUR POS: {} \t\t({})".format(node.value, node.state.is_vampire, node.state.get_current_pos()[0], level))
                for child in node.children:
                    self.print_tree(child, level + 1)


def find_children(game_map: GameMap, parent: Node):
    moves = game_map.possible_moves()
    maps = new_maps(game_map, moves)

    for game_map, move in zip(maps, moves):
        leaf_node = Node(game_map)
        leaf_node.parent = parent
        parent.addChild(leaf_node)

    return