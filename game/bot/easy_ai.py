import random
from ai import AbstractAI

def make_move(board):
    available_moves = [(x, y) for x in range(board.size) for y in range(board.size) if board.is_empty(x, y)]
    move = random.choice(available_moves)
    return move

class EasyAI(AbstractAI):
    def make_move(self):
        return super().make_move()
