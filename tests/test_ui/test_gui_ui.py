import unittest
from ui import GUI
import tkinter as tk

class TestGUI(unittest.TestCase):
    def test_display_board(self):
        gui = GUI()
        board = [...]
        gui.display_board(board)

    def test_get_user_input(self):
        gui = GUI()
        user_input = gui.get_user_input()
        self.assertIsNotNone(user_input)

    def test_update_board(self):
        gui = GUI()
        board = [...]
        gui.update_board(board)

if __name__ == '__main__':
    unittest.main()
