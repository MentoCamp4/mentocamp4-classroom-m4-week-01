import unittest
from abbreviate_two_word_name import abbrev_name

class TestAbbreviateTwoWordName(unittest.TestCase):

    def test_abbrev_name(self):
        # 測試名字"John Smith"的縮寫
        self.assertEqual(abbrev_name("John Smith"), "J.S")
        # 測試名字"Alice Johnson"的縮寫
        self.assertEqual(abbrev_name("Alice Johnson"), "A.J")
        # 測試名字"Bob Brown"的縮寫
        self.assertEqual(abbrev_name("Bob Brown"), "B.B")

if __name__ == '__main__':
    unittest.main()
