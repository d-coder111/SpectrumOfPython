import random, pickle

class Ship:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.hit = False

    def is_sunk(self):
        return self.hit

    def get_size(self):
        return self.size

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == ' '

    def get_cell(self, x, y):
        return self.board[x][y]

    def display_board(self):
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(i, ' '.join(cell for cell in row))

class ShipBattle:
    def __init__(self, game_board):
        self.game_board = game_board
        self.ships = [Ship(0, 0, 2), Ship(1, 1, 3), Ship(2, 2, 4)]
        self.hit_count = 0
        self.ship_count = len(self.ships)
        self.timer = 60
        self.player_turn = True
        self.score = 0

    def get_ship_by_coordinates(self, x, y):
        for ship in self.ships:
            if ship.x == x and ship.y == y:
                return ship
        return None

    def check_ship_sunk(self, ship):
        return ship.is_sunk()

    def game_over(self):
        return self.timer <= 0 or all(ship.is_sunk() for ship in self.ships)

    def get_winner(self):
        if self.hit_count == self.ship_count:
            return "Player"
        else:
            return "AI"

    def ai_make_move(self):
        possible_moves = [(x, y) for x in range(self.game_board.size) for y in range(self.game_board.size) if self.game_board.is_valid_move(x, y)]
        if not possible_moves:
            return None
        return random.choice(possible_moves)

    def make_move(self, x, y):
        ship = self.get_ship_by_coordinates(x, y)
        if ship:
            ship.hit = True
            self.hit_count += 1
            self.score += 1
        else:
            self.game_board.board[x][y] = 'X'

    def display_board(self):
        self.game_board.display_board()

    def play_game(self):
        self.timer = 60
        while True:
            self.display_board()
            if self.player_turn:
                print(f"Time: {self.timer} seconds")
                x, y = map(int, input("enter traverse coordinates (x y): ").split())
                self.make_move(x, y)
                self.player_turn = False
            else:
                ai_x, ai_y = self.ai_make_move()
                if ai_x is None:
                    print("AI can't make move right now!")
                    break
                self.make_move(ai_x, ai_y)
                self.player_turn = True
            if self.game_over():
                print("Game end!")
                if all(ship.is_sunk() for ship in self.ships):
                    print("You are won!")
                else:
                    print("AI won!")
                print(f"Your point: {self.score}")
                print(f"Game time: {60 - self.timer} seconds")
                break
            self.timer -= 1

    def save_game(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_game(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
