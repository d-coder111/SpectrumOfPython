import tkinter as tk
from game import GameLogic

class GameBoardGUI:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.draw_game_board()
        self.game_logic = GameLogic()

        self.place_ship_button = tk.Button(master, text="Разместить корабль", command=self.place_ship)
        self.place_ship_button.pack()

    def draw_game_board(self):
        for i in range(10):
            for j in range(10):
                self.canvas.create_rectangle(i*40, j*40, (i+1)*40, (j+1)*40, fill='dark blue')

    def place_ship(self):
        self.game_logic.place_ship()
        self.update_game_state()

    def update_game_state(self):
        self.canvas.delete("all")
        self.draw_game_board()
        self.canvas.create_rectangle(100, 100, 140, 140, fill='green')

root = tk.Tk()
game_board_gui = GameBoardGUI(root)
root.mainloop()
