import random
from ai import AbstractAI

def make_move(board):
    available_moves = [(x, y) for x in range(board.size) for y in range(board.size) if board.is_empty(x, y)]
    scores = []
    for move in available_moves:
        score = evaluate_move(board, move)
        scores.append((move, score))
    best_move = max(scores, key=lambda x: x[1])[0]
    return best_move

class HardAI(AbstractAI):
    def make_move(self):
        pass

def evaluate_move(self, board, player):
    pass
