import unittest
from utils import algebra

class TestAlgebra(unittest.TestCase):
    def test_expression(self):
        expression = 'x + 2 * y'
        x, y = 1, 2
        result = algebra.expression(expression, x, y)
        self.assertEqual(result, 5)

    def test_equation(self):
        equation = 'x + 2 * y = 5'
        x, y = 1, 2
        result = algebra.equation(equation, x, y)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
