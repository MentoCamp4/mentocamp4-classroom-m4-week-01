import unittest
from unique_in_order import unique_in_order

class TestUniqueInOrder(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(unique_in_order(""), [])

    def test_string_input(self):
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order("12233"), ['1', '2', '3'])
        self.assertEqual(unique_in_order("ABBCcAD"), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_list_input(self):
        self.assertEqual(unique_in_order(['A', 'A', 'B', 'C', 'C', 'D']), ['A', 'B', 'C', 'D'])

if __name__ == '__main__':
    unittest.main()
