import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Matching Game")
        self.buttons = []
        self.first = None
        self.second = None
        self.pairs_found = 0
        self.card_values = self.generate_card_values()

        self.create_board()

    def generate_card_values(self):
        """Generates pairs of card values and shuffles them."""
        values = list(range(1, 9)) * 2  # Create pairs from 1 to 8
        random.shuffle(values)  # Shuffle the values
        return values

    def create_board(self):
        """Creates the game board with buttons."""
        for i in range(4):  # 4 rows
            row = []
            for j in range(4):  # 4 columns
                button = tk.Button(self.root, text="", width=8, height=4, 
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, row, col):
        """Handles the logic when a card is clicked."""
        if self.first and self.second:
            return  # Don't allow more than two selections at a time

        button = self.buttons[row][col]

        if not button['text']:  # Only act if button hasn't been flipped
            button['text'] = str(self.card_values[row * 4 + col])

            if not self.first:
                self.first = (row, col)
            elif not self.second:
                self.second = (row, col)

                self.root.after(1000, self.check_match)  # Wait 1 second and check

    def check_match(self):
        """Checks if two selected cards are a match."""
        first_row, first_col = self.first
        second_row, second_col = self.second

        first_value = self.card_values[first_row * 4 + first_col]
        second_value = self.card_values[second_row * 4 + second_col]

        if first_value == second_value:
            self.pairs_found += 1
        else:
            self.buttons[first_row][first_col]['text'] = ""
            self.buttons[second_row][second_col]['text'] = ""

        self.first = None
        self.second = None

        if self.pairs_found == 8:
            self.show_win_message()

    def show_win_message(self):
        """Displays a win message when all pairs are found."""
        win_message = tk.Label(self.root, text="Congratulations! You've found all pairs!", font=('Arial', 16))
        win_message.grid(row=4, column=0, columnspan=4)

# Running the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
