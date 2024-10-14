class GameRoom:
    def __init__(self, game_board, players):
        self.game_board = game_board
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def start_game(self):
        self.game_board.place_ships(...)

        while True:
            x, y = self.get_current_player_move()

            if self.game_board.check_hit(x, y):
                print("Hit!")
            else:
                print("Miss!")

            if self.game_board.check_win():
                print("You win!")
                break

    def end_game(self):
        pass

    def get_current_player_move(self):
        pass
