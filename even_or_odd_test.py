import unittest
from even_or_odd import even_or_odd

class TestEvenOrOdd(unittest.TestCase):

    def test_even_input(self):
        self.assertEqual(even_or_odd(4), "Even")
        self.assertEqual(even_or_odd(0), "Even")
        self.assertEqual(even_or_odd(100), "Even")

    def test_odd_input(self):
        self.assertEqual(even_or_odd(7), "Odd")
        self.assertEqual(even_or_odd(33), "Odd")
        self.assertEqual(even_or_odd(99), "Odd")

if __name__ == '__main__':
    unittest.main()