import unittest
from array_diff import array_diff

class TestArrayDiff(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(array_diff([1,2], [1]), [2])
        self.assertEqual(array_diff([1,2,2], [1]), [2,2])
        self.assertEqual(array_diff([1,2,2], [2]), [1])
        self.assertEqual(array_diff([1,2,2], []), [1,2,2])
        self.assertEqual(array_diff([], [1,2]), [])

if __name__ == '__main__':
    unittest.main()