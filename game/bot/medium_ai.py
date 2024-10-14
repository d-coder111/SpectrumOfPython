import random
from ai import AbstractAI

class MediumAI(AbstractAI):
    def make_move(self):
        pass

def make_move(board):
    available_moves = [(x, y) for x in range(board.size) for y in range(board.size) if board.is_empty(x, y)]
    row_or_col = random.choice(['row', 'col'])
    if row_or_col == 'row':
        row = random.randint(0, board.size - 1)
        move = (row, random.randint(0, board.size - 1))
    else:
        col = random.randint(0, board.size - 1)
        move = (random.randint(0, board.size - 1), col)
    return move
