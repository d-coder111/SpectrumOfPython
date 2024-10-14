import random

class AbstractAI:
    def __init__(self, game_board):
        self.game_board = game_board
        self.probability_matrix = [[1.0 for _ in range(game_board.size)] for _ in range(game_board.size)]

    def make_move(self):
        raise NotImplementedError("Subclasses must implement make_move")

    def update_probability_matrix(self):
        for i in range(self.game_board.size):
            for j in range(self.game_board.size):
                if self.game_board.board[i][j] == 'X':
                    self.update_probability_matrix_cell(i, j, -0.1)
                elif self.game_board.board[i][j] == 'O':
                    self.update_probability_matrix_cell(i, j, 0.1)

    def update_probability_matrix_cell(self, x, y, delta):
        for i in range(max(0, x-1), min(self.game_board.size, x+2)):
            for j in range(max(0, y-1), min(self.game_board.size, y+2)):
                self.probability_matrix[i][j] += delta
