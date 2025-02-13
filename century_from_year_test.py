import unittest
from century_from_year import century

class TestCenturyFromYear(unittest.TestCase):

    def test_century(self):
        self.assertEqual(century(1705), 18)
        self.assertEqual(century(1900), 19)
        self.assertEqual(century(2000), 20)
        self.assertEqual(century(2001), 21)

if __name__ == '__main__':
    unittest.main()
