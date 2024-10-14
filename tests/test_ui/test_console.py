import unittest
from ui import ConsoleUI

class TestConsoleUI(unittest.TestCase):
    def test_display_board(self):
        console_ui = ConsoleUI()
        board = [...]
        console_ui.display_board(board)

    def test_get_user_input(self):
        console_ui = ConsoleUI()
        user_input = console_ui.get_user_input()
        self.assertIsNotNone(user_input)

if __name__ == '__main__':
    unittest.main()
