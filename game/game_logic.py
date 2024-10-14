from game import GameState

class GameLogic:
    def __init__(self, game_board):
        self.game_board = game_board
        self.winners = {}
        self.game_state = GameState.IN_PROGRESS
        self.scores = {'X': 0, 'O': 0}

    def validate_input(self, input_value):
        if not isinstance(input_value, int):
            raise ValueError("Input must be an integer")
        if input_value < 0 or input_value > self.game_board.size - 1:
            raise ValueError("The input must be in the range 0 to {}".format(self.game_board.size - 1))
        return input_value

    def check_win(self, x, y):
        if self.check_win_horizontal(x, y) or \
           self.check_win_vertical(x, y) or \
           self.check_win_diagonal(x, y):
            return True
        return False

    def check_win_horizontal(self, x, y):
        if y <= self.game_board.size - 3 and all(self.game_board.board[x][y+k] == self.game_board.board[x][y] for k in range(3)):
            self.winners[(x, y)] = self.game_board.board[x][y]
            return True
        return False

    def check_win_vertical(self, x, y):
        if x <= self.game_board.size - 3 and all(self.game_board.board[x+k][y] == self.game_board.board[x][y] for k in range(3)):
            self.winners[(x, y)] = self.game_board.board[x][y]
            return True
        return False

    def check_win_diagonal(self, x, y):
        if x <= self.game_board.size - 3 and y <= self.game_board.size - 3 and all(self.game_board.board[x+k][y+k] == self.game_board.board[x][y] for k in range(3)):
            self.winners[(x, y)] = self.game_board.board[x][y]
            return True
        if x <= self.game_board.size - 3 and y >= 2 and all(self.game_board.board[x+k][y-k] == self.game_board.board[x][y] for k in range(3)):
            self.winners[(x, y)] = self.game_board.board[x][y]
            return True
        return False

    def make_move(self, player, x, y):
        try:
            x = self.validate_input(x)
            y = self.validate_input(y)
            if not self.is_valid_move(x, y):
                raise ValueError("Invalid move: ({}, {}) is out of bounds".format(x, y))
            if player not in ['X', 'O']:
                raise ValueError("Invalid player: {}".format(player))
            self.game_board.board[x][y] = player
            if self.check_win(x, y):
                self.game_state = GameState.WIN
                self.scores[player] += 1
                self.log_game_event("Win", player)
        except ValueError as e:
            print(f"Error: Invalid input. {e}")
        except Exception as e:
            print(f"Error: Unknown error. {e}")

    def is_valid_move(self, x, y):
        try:
            x = self.validate_input(x)
            y = self.validate_input(y)
            return 0 <= x < self.game_board.size and 0 <= y < self.game_board.size and self.game_board.board[x][y] == 0
        except ValueError as e:
            print(f"Error: Invalid input. {e}")
            return False

    def play(self, player1, player2):
        try:
            while True:
                if self.game_state != GameState.IN_PROGRESS:
                    break
                self.print_board()
                x, y = player1.make_move(self.game_board)
                self.make_move('X', x, y)
                if self.check_win(x, y):
                    self.game_state = GameState.WIN
                    self.update_score('X')
                    break

                self.print_board()
                x, y = player2.make_move(self.game_board)
                self.make_move('O', x, y)
                if self.check_win(x, y):
                    self.game_state = GameState.WIN
                    self.update_score('O')
                    break

                if self.is_draw():
                    self.game_state = GameState.DRAW
                    break
            self.print_scores()
            self.print_winner()
        except ValueError as e:
            print(f"Error: Invalid input. {e}")
        except Exception as e:
            print(f"Error: {e}")

    def is_draw(self):
        for i in range(self.game_board.size):
            for j in range(self.game_board.size):
                if self.game_board.board[i][j] == 0:
                    return False
        return True
    
    def get_game_board(self):
        return self.game_board.board

    def update_score(self, winner):
        self.scores[winner] += 1

    def get_game_state(self):
        return self.game_state
    
    def get_player_scores(self):
        return self.scores

    def get_scores(self):
        return self.scores

    def get_winner(self):
        if self.game_state == GameState.WIN:
            return list(self.winners.values())[0]
        return None

    def reset(self):
        self.game_board.reset()
        self.game_state = GameState.IN_PROGRESS
        self.scores = {'X': 0, 'O': 0}
        self.winners = {}

    def log_game_event(self, event, player):
        print(f"{event} by {player}")

    def get_winner_position(self):
        if self.game_state == GameState.WIN:
            return list(self.winners.keys())[0]
        return None

    def print_board(self):
        print("Current state of the playing field:")
        for row in self.game_board.board:
            print(" ".join(str(cell) for cell in row))

    def print_scores(self):
        print("Current player accounts:")
        print("X:", self.scores['X'])
        print("O:", self.scores['O'])

    def print_winner(self):
        if self.game_state == GameState.WIN:
            print("Game winner:", self.get_winner())
        else:
            print("Game is not over yet.")
