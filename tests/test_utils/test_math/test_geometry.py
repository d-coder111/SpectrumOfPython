import unittest
from utils import geometry

class TestGeometry(unittest.TestCase):
    def test_distance(self):
        x1, y1 = 1, 2
        x2, y2 = 4, 6
        distance = geometry.distance(x1, y1, x2, y2)
        self.assertAlmostEqual(distance, 5.0)

    def test_angle(self):
        x1, y1 = 1, 2
        x2, y2 = 4, 6
        angle = geometry.angle(x1, y1, x2, y2)
        self.assertAlmostEqual(angle, 45.0)

if __name__ == '__main__':
    unittest.main()
