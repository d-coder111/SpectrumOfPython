from ui import UIAdapter

class CLI:
    def __init__(self, game):
        self.game = game

    def display_game_board(self):
        print("Board:")
        for row in self.game.game_board.board:
            print(' | '.join(row))
            print('-' * (self.game.game_board.size * 4 - 1))

    def parse_command(self, command):
        if command == "place_ships":
            self.game.place_ships()
        elif command == "make_move":
            x, y = input("Enter traverse coordinates (x y): ").split()
            self.game.make_move(int(x), int(y))
        elif command == "display_board":
            self.display_game_board()
        elif command == "quit":
            print("Good bye!")
            return False
        else:
            print("Wrong command. try again.")
        return True

    def start_game(self):
        print("Welcome to the game!")
        while True:
            command = input("Enter the command (place_ships, make_move, display_board, quit): ")
            if not self.parse_command(command):
                break
