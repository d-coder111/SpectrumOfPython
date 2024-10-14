import unittest
from utils import validation

class TestStringValidation(unittest.TestCase):
    def test_is_empty(self):
        empty_string = ""
        non_empty_string = "Hello"
        self.assertTrue(validation.is_empty(empty_string))
        self.assertFalse(validation.is_empty(non_empty_string))

    def test_matches_pattern(self):
        pattern = "^[a-zA-Z]+$"
        matching_string = "Hello"
        non_matching_string = "Hello123"
        self.assertTrue(validation.matches_pattern(matching_string, pattern))
        self.assertFalse(validation.matches_pattern(non_matching_string, pattern))

if __name__ == '__main__':
    unittest.main()
