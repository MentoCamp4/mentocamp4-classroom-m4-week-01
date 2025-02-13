import unittest
from find_smallest_integer import find_smallest_int

class TestFindSmallestInteger(unittest.TestCase):

    def test_find_smallest_int(self):
        self.assertEqual(find_smallest_int([4, 3, 7, 1, 2, 8]), 1)
        self.assertEqual(find_smallest_int([10, 20, 30, 40, 50]), 10)
        self.assertEqual(find_smallest_int([-5, -2, 0, 3, 6]), -5)
        self.assertEqual(find_smallest_int([100, 200, 300, 400, 500]), 100)
        self.assertEqual(find_smallest_int([5]), 5)

if __name__ == '__main__':
    unittest.main()
