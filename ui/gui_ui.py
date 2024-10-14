import tkinter as tk
from game.ship_battle import ShipBattle
from ui import UIAdapter

class GUIUI(UIAdapter):
    def __init__(self, game_logic):
        self.game_logic = game_logic
        self.root = tk.Tk()
        self.root.title("Sea Battle")
        self.create_widgets()

    def create_widgets(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.board_labels = []
        for i in range(self.game_logic.game_board.size):
            row = []
            for j in range(self.game_logic.game_board.size):
                label = tk.Label(self.board_frame, text="", width=2)
                label.grid(row=i, column=j)
                row.append(label)
            self.board_labels.append(row)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_game)
        self.play_button.pack()

    def display_game_board(self, game_board):
        for i in range(self.game_logic.game_board.size):
            for j in range(self.game_logic.game_board.size):
                if self.game_logic.game_board.board[i][j] == 'S':
                    self.board_labels[i][j].config(text='S')
                elif self.game_logic.game_board.board[i][j] == 'X':
                    self.board_labels[i][j].config(text='X')
                elif self.game_logic.game_board.board[i][j] == 'O':
                    self.board_labels[i][j].config(text='O')
                else:
                    self.board_labels[i][j].config(text='.')

    def display_player_statistics(self, player_stats):
        stats_label = tk.Label(self.root, text=f"Win: {player_stats.wins}, Loses: {player_stats.losses}")
        stats_label.pack()

    def create_room(self, room_name):
        room_label = tk.Label(self.root, text=f"Room: {room_name}")
        room_label.pack()

    def play_game(self):
        self.game_logic.place_ships()
        self.update_board()
        self.display_player_statistics(self.game_logic.player_stats)
        self.create_room("My room.")
        self.game_loop()

    def game_loop(self):
        while True:
            if self.game_logic.is_winner():
                self.display_winner_message()
                break
            self.update_board()
            self.root.update_idletasks()
            self.root.update()

    def update_board(self):
        if self.game_logic.is_winner():
            self.display_winner_message()
        else:
            for i in range(self.game_logic.game_board.size):
                for j in range(self.game_logic.game_board.size):
                    if self.game_logic.game_board.board[i][j] == 'S':
                        self.board_labels[i][j].config(text='S')
                    elif self.game_logic.game_board.board[i][j] == 'X':
                        self.board_labels[i][j].config(text='X')
                    elif self.game_logic.game_board.board[i][j] == 'O':
                        self.board_labels[i][j].config(text='O')
                    else:
                        self.board_labels[i][j].config(text='.')

    def handle_cell_click(self, event):
        if self.game_logic.is_valid_move(event.x, event.y):
            self.game_logic.make_move(event.x, event.y)
            self.update_board()
        else:
            self.display_invalid_move_message()

    def handle_ship_placement(self):
        ship_type = tk.simpledialog.askinteger("Ship Type", "Enter ship type (1-5):")
        ship_x = tk.simpledialog.askinteger("Ship X", "Enter ship X coordinate:")
        ship_y = tk.simpledialog.askinteger("Ship Y", "Enter ship Y coordinate:")
        self.game_logic.place_ship(ship_type, ship_x, ship_y)
        self.update_board()

    def display_winner_message(self):
        winner_label = tk.Label(self.root, text="Congratulations, you won!")
        winner_label.pack()

    def display_invalid_move_message(self):
        invalid_move_label = tk.Label(self.root, text="Invalid move, try again!")
        invalid_move_label.pack()
