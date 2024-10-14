import unittest
from utils import compression

class TestCompression(unittest.TestCase):
    def test_compress_file(self):
        file_path = 'path/to/test/file.txt'
        compressed_file_path = 'path/to/test/compressed_file.txt.gz'
        compression.compress_file(file_path, compressed_file_path)

    def test_decompress_file(self):
        compressed_file_path = 'path/to/test/compressed_file.txt.gz'
        decompressed_file_path = 'path/to/test/decompressed_file.txt'
        compression.decompress_file(compressed_file_path, decompressed_file_path)

if __name__ == '__main__':
    unittest.main()
