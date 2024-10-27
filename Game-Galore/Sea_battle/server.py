import socket
import threading
import json
from game import Game
from ai import AIPlayer

class GameServer:
    def __init__(self, host='localhost', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        self.players = []
        self.game = Game()
        self.ai_player = AIPlayer("AI")

    def handle_client(self, client_socket, player_number):
        while True:
            try:
                if self.game.current_player.is_ai:
                    row, col = self.ai_player.make_move(self.game.board2)
                    print(f"{self.ai_player.name} chose the coordinates: ({row}, {col})")
                    self.game.shoot(row, col)
                    game_state = self.get_game_state()
                    self.broadcast(game_state)
                else:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    if data == "move":
                        move = client_socket.recv(1024).decode('utf-8')
                        row, col = map(int, move.split())
                        self.game.shoot(row, col)
                        game_state = self.get_game_state()
                        self.broadcast(game_state)
                    elif data == "get_state":
                        game_state = self.get_game_state()
                        client_socket.send(json.dumps(game_state).encode('utf-8'))
            except ConnectionResetError:
                break
            except json.JSONDecodeError:
                print("Received an invalid JSON message.")
                break

        client_socket.close()

    def broadcast(self, game_state):
        for player in self.players:
            player.send(json.dumps(game_state).encode('utf-8'))

    def get_game_state(self):
        return {
            'board1': self.game.board1.grid,
            'board2': self.game.board2.grid,
            'current_player': self.game.current_player.name,
            'is_game_over': self.game.is_game_over
        }

    def start(self):
        print("Server started, waiting for players...")
        while len(self.players) < 2:
            client_socket, addr = self.server_socket.accept()
            print(f"Player {len(self.players) + 1} connected from {addr}")
            self.players.append(client_socket)
            if len(self.players) == 2:
                self.game.current_player = self.game.human_player
                threading.Thread(target=self.handle_client, args=(client_socket, len(self.players))).start()

if __name__ == "__main__":
    server = GameServer()
    server.start()
