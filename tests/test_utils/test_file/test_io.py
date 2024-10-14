import unittest
from utils import io

class TestIO(unittest.TestCase):
    def test_read_file(self):
        file_path = 'path/to/test/file.txt'
        content = io.read_file(file_path)
        self.assertIsNotNone(content)

    def test_write_file(self):
        file_path = 'path/to/test/file.txt'
        content = 'Test content'
        io.write_file(file_path, content)

if __name__ == '__main__':
    unittest.main()
