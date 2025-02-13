import unittest
from square import is_square

class TestIsSquare(unittest.TestCase):

    def test_is_square_1(self):
        self.assertEqual(is_square(25), True)

    def test_is_square_2(self):
        self.assertEqual(is_square(4), True)

    def test_is_square_3(self):
        self.assertEqual(is_square(5), False)

    def test_is_square_4(self):
        self.assertEqual(is_square(0), True)

    def test_is_square_5(self):
        self.assertEqual(is_square(1), True)

    def test_is_square_6(self):
        self.assertEqual(is_square(9), True)

if __name__ == '__main__':
    unittest.main()