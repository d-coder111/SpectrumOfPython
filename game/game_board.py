class GameBoard:
    DEFAULT_SIZE = 10

    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def make_move(self, row, col, player):
        if not self.is_valid_move(row, col):
            print("Некорректный ход! Попробуйте снова.")
            return False

        if self.board[row][col] != ' ':
            print("Клетка уже занята!")
            return False

        self.board[row][col] = player
        return True

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset(self):
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def check_winner(self):
        for i in range(self.size):
            if self.board[i].count(self.board[i][0]) == self.size and self.board[i][0] != ' ':
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] for j in range(self.size)) and self.board[0][i] != ' ':
                return self.board[0][i]

        if all(self.board[i][i] == self.board[0][0] for i in range(self.size)) and self.board[0][0] != ' ':
            return self.board[0][0]
        if all(self.board[i][self.size - i - 1] == self.board[0][self.size - 1] for i in range(self.size)) and self.board[0][self.size - 1] != ' ':
            return self.board[0][self.size - 1]

        return None

    def get_board_state(self):
        return [''.join(row) for row in self.board]

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
