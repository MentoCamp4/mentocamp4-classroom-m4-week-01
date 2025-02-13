import unittest
from count_duplicates import count_duplicates

class TestCountingDuplicates(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_duplicates(""), 0)

    def test_no_duplicates(self):
        self.assertEqual(count_duplicates("abcde"), 0)

    def test_with_duplicates(self):
        self.assertEqual(count_duplicates("aabbcde"), 2)

    def test_case_insensitive(self):
        self.assertEqual(count_duplicates("AaBbCde"), 2)

    def test_mixed_cases(self):
        self.assertEqual(count_duplicates("Indivisibilities"), 2)

if __name__ == "__main__":
    unittest.main()
