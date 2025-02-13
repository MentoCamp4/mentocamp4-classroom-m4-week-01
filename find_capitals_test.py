import unittest
from find_capitals import find_capitals

class TestFindCapitals(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(find_capitals(""), "")

    def test_no_capitals(self):
        self.assertEqual(find_capitals("hello world"), "")

    def test_some_capitals(self):
        self.assertEqual(find_capitals("The Quick Brown Fox"), "TQBF")
        self.assertEqual(find_capitals("Python is Fun"), "PF")

if __name__ == '__main__':
    unittest.main()
