from ui import UIAdapter

class ConsoleUI(UIAdapter):
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def display_game_board(self, game_board):
        self.game_logic.game_board.print_board()

    def display_player_statistics(self, player_stats):
        print("Player statistics:")
        print("Wins:", player_stats.wins)
        print("Losses:", player_stats.losses)

    def create_room(self, room_name):
        print(f"Room '{room_name}' created successfully!")

    def play_game(self):
        self.game_logic.place_ships()
        while True:
            self.display_game_board(self.game_logic.game_board)
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))

            if self.game_logic.game_board.check_hit(x, y):
                print("Hit!")
            else:
                print("Miss!")

            if self.game_logic.game_board.check_win():
                print("You won!")
                break

    def print_board(self, board: list) -> None:
        for row in board:
            print(" ".join(row))

    def get_user_input(self) -> str:
        return input("Enter your move (x and y coordinates separated by space): ")

    def update_board(self, board: list, move: str) -> None:
        x, y = map(int, move.split())
        board[y][x] = 'X' if self.game_logic.game_board.check_hit(x, y) else 'O'
