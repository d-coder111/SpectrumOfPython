import unittest
from game import GameBoard

class TestGameBoard(unittest.TestCase):
    def test_init_board(self):
        board = GameBoard()
        self.assertIsNotNone(board)

    def test_generate_random_board(self):
        board = GameBoard()
        random_board = board.generate_random_board()
        self.assertIsNotNone(random_board)

    def test_is_valid_board(self):
        board = GameBoard()
        valid = board.is_valid_board([...])
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()
