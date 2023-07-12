#!/usr/bin/python
from argparse import ArgumentParser
from src.player import play_game
from src.server_communication import ServerInterface

# python main.py 'server' 'port' Name

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(dest='ip', default='localhost', type=str, help='IP address the connection should be made to.')
    parser.add_argument(dest='port', default='5555', type=int, help='Chosen port for the connection.')
    parser.add_argument(dest='name', type=str, help='Name of the player')

    args = parser.parse_args()

    try:
        server = ServerInterface(args.ip,args.port,args.name)

        play_game(server)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Game Ended!!!")
