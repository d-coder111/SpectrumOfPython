import socket
import json

class GameClient:
    def __init__(self, host='localhost', port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_move(self, row, col):
        move_data = {'action': 'move', 'row': row, 'col': col}
        self.client_socket.send(json.dumps(move_data).encode('utf-8'))

    def get_game_state(self):
        self.client_socket.send("get_state".encode('utf-8'))
        data = self.client_socket.recv(1024).decode('utf-8')
        return json.loads(data)

    def play(self):
        while True:
            game_state = self.get_game_state()
            print(f"Current player: {game_state['current_player']}")
            print("Board 1:", game_state['board1'])
            print("Board 2:", game_state['board2'])

            if game_state['is_game_over']:
                print("Game Over!")
                break

            while True:
                try:
                    row = int(input("Enter row (0-9): "))
                    col = int(input("Enter column (0-9): "))
                    if row < 0 or row >= 10 or col < 0 or col >= 10:
                        print("Coordinates out of bounds! Please enter values between 0 and 9.")
                        continue
                    self.send_move(row, col)
                    break
                except ValueError:
                    print("Invalid input! Please enter integers.")

if __name__ == "__main__":
    client = GameClient()
    client.play()
