import random

class AIPlayer:
    def __init__(self, name):
        self.name = name
        self.previous_moves = set()

    def make_move(self, board):
        while True:
            row = random.randint(0, len(board.grid) - 1)
            col = random.randint(0, len(board.grid[0]) - 1)
            if (row, col) not in self.previous_moves:
                self.previous_moves.add((row, col))
                return (row, col)
