import random

class Player:
    def __init__(self, name):
        self.name = name
        self.is_ai = False

class HumanPlayer(Player):
    def __init__(self):
        name = input("Enter player name: ")
        super().__init__(name)

    def setup_ships(self, board):
        choice = input("Do you want to place ships manually or automatically? (manual/auto): ")
        if choice == "manual":
            self.place_ships_manually(board)
        else:
            self.place_ships_automatically(board)

    def get_move(self):
        while True:
            try:
                row = int(input("Enter line number (0-9): "))
                col = int(input("Enter column number (0-9): "))
                if 0 <= row < 10 and 0 <= col < 10:
                    return row, col
                else:
                    print("The coordinates must be in the range from 0 to 9.")
            except ValueError:
                print("Invalid input, please try again.")

    def place_ships_manually(self, board):
        pass

    def place_ships_automatically(self, board):
        pass

class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.is_ai = True

    def get_move(self):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        print(f"{self.name} (AI) chooses coordinates: ({row}, {col})")
        return row, col
