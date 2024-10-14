import unittest
from game import AI

class TestAI(unittest.TestCase):
    def test_make_move(self):
        ai = AI()
        board = [...]
        move = ai.make_move(board)
        self.assertIsNotNone(move)

    def test_evaluate_position(self):
        ai = AI()
        board = [...] 
        evaluation = ai.evaluate_position(board)
        self.assertIsNotNone(evaluation)

if __name__ == '__main__':
    unittest.main()
