import unittest
from count_sheep import count_sheep

class TestCountSheep(unittest.TestCase):

    def test_count_sheep_1(self):
        self.assertEqual(count_sheep([True, True, True, False, True]), 4)

    def test_count_sheep_2(self):
        self.assertEqual(count_sheep([True, True, False, False, True, True]), 4)

    def test_count_sheep_3(self):
        self.assertEqual(count_sheep([False, False, False, False]), 0)

    def test_count_sheep_4(self):
        self.assertEqual(count_sheep([]), 0)

    def test_count_sheep_5(self):
        self.assertEqual(count_sheep([True, False, True, True, False]), 3)

if __name__ == '__main__':
    unittest.main()