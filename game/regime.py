class GameRegime:
    def __init__(self, game_board, ai):
        self.game_board = game_board
        self.ai = ai

    def play_single_player(self):
        self.game_board.place_ships(...) 

        while True:
            x, y = self.ai.get_move()

            if self.game_board.check_hit(x, y):
                print("Hit!")
            else:
                print("Miss!")

            if self.game_board.check_win():
                print("You win!")
                break

    def play_multi_player(self):
        pass
