import unittest
from utils import formatting

class TestStringFormatting(unittest.TestCase):
    def test_format_string(self):
        template = "Hello, {}!"
        variable = "World"
        formatted_string = formatting.format_string(template, variable)
        self.assertEqual(formatted_string, "Hello, World!")

    def test_trim_string(self):
        original_string = "   Hello, World!   "
        trimmed_string = formatting.trim_string(original_string)
        self.assertEqual(trimmed_string, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
