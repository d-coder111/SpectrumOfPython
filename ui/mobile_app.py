from ui import UIAdapter

class KeyboardUIAdapter(UIAdapter):
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def display_game_board(self, game_board):
        print("Keyboard UI: Game Board")
        print(game_board.board)

    def display_player_statistics(self, player_stats):
        print("Keyboard UI: Player Statistics")
        print("Wins:", player_stats.wins)
        print("Losses:", player_stats.losses)

    def create_room(self, room_name):
        pass
