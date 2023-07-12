from src.client import ClientSocket

class ServerInterface:
    def __init__(self, ip, port, name):
        self.ip = ip
        self.port = port
        self.name = name

        # create connection with server
        self.client = ClientSocket(self.ip, self.port)
        self.client.send_nme(self.name)

        for _ in range(0, 4):
            key, value = self.client.get_message()
            self._parse_message(key, value)


    def _parse_message(self, key, value, isUpdate=False):
        if key == 'set':
            self.board_height, self.board_width = value
        elif key == 'hme':
            self.init_pos = value
        elif key == 'map':
            self.map = value
        elif key == 'upd':
            self.update = value
            if isUpdate:
                isUpdate.update_map(value)
        elif key == 'hum':
            self.homes = value
        else:
            raise ValueError('Unexpected command from server!')

    def send_move(self, nb_players, current_pos, target_pos):
        self.client.send_mov(1, [current_pos, nb_players, target_pos])

    def update_board(self, board):
        key, value = self.client.get_message()
        self._parse_message(key, value, board)

        return key
