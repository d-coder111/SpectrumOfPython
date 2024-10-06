# Chess game with basic piece movement logic

class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        raise NotImplementedError("This method should be overridden by subclasses")


class Pawn(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos

        if self.color == 'white':
            if row_start == 6 and row_start - row_end == 2 and col_start == col_end:
                return True
            if row_start - row_end == 1 and col_start == col_end:
                return True
        else:  # black
            if row_start == 1 and row_end - row_start == 2 and col_start == col_end:
                return True
            if row_end - row_start == 1 and col_start == col_end:
                return True
        return False


class Rook(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        return row_start == row_end or col_start == col_end


class Knight(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        row_diff = abs(row_start - row_end)
        col_diff = abs(col_start - col_end)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


class Bishop(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        return abs(row_start - row_end) == abs(col_start - col_end)


class Queen(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        return abs(row_start - row_end) == abs(col_start - col_end) or row_start == row_end or col_start == col_end


class King(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        row_start, col_start = start_pos
        row_end, col_end = end_pos
        return abs(row_start - row_end) <= 1 and abs(col_start - col_end) <= 1


class Board:
    def __init__(self):
        self.board = self.setup_board()

    def setup_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        for i in range(8):
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')

        board[0][0] = board[0][7] = Rook('black')
        board[7][0] = board[7][7] = Rook('white')

        board[0][1] = board[0][6] = Knight('black')
        board[7][1] = board[7][6] = Knight('white')

        board[0][2] = board[0][5] = Bishop('black')
        board[7][2] = board[7][5] = Bishop('white')

        board[0][3] = Queen('black')
        board[7][3] = Queen('white')

        board[0][4] = King('black')
        board[7][4] = King('white')

        return board

    def display(self):
        for row in self.board:
            row_display = []
            for piece in row:
                if piece is None:
                    row_display.append(".")
                else:
                    row_display.append(piece.__class__.__name__[0] + ('w' if piece.color == 'white' else 'b'))
            print(" ".join(row_display))
        print()

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece(start_pos)
        if piece is not None and piece.is_valid_move(start_pos, end_pos, self.board):
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = None
            return True
        return False

    def get_piece(self, position):
        row, col = position
        return self.board[row][col]


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn.capitalize()}'s turn")

            try:
                start = input("Enter start position (e.g., 6 0 for row 6, column 0): ").split()
                end = input("Enter end position (e.g., 5 0 for row 5, column 0): ").split()
                start_pos = (int(start[0]), int(start[1]))
                end_pos = (int(end[0]), int(end[1]))

                piece = self.board.get_piece(start_pos)

                if piece is None or piece.color != self.current_turn:
                    print("Invalid move! Try again.")
                    continue

                if self.board.move_piece(start_pos, end_pos):
                    self.switch_turn()
                else:
                    print("Invalid move! Try again.")

            except (ValueError, IndexError):
                print("Invalid input! Please use the correct format (e.g., 6 0 for row 6, column 0).")


if __name__ == "__main__":
    game = Game()
    game.play()
