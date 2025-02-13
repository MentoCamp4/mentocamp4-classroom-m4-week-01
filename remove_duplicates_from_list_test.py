import unittest
from remove_duplicates_from_list import distinct

class TestRemoveDuplicatesFromList(unittest.TestCase):

    def test_distinct(self):
        self.assertEqual(distinct([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(distinct([1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(distinct([1, 1, 1, 1, 1]), [1])
        self.assertEqual(distinct([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
        self.assertEqual(distinct([]), [])

if __name__ == '__main__':
    unittest.main()
