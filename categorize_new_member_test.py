import unittest
from categorize_new_member import categorize_new_member

class TestCategorizeNewMember(unittest.TestCase):

    # 測試 senior 成員的情況
    def test_senior_members(self):
        self.assertEqual(categorize_new_member([(65, 8.0), (70, 7.5)]), ["Senior", "Senior"])

    # 測試 open 成員的情況
    def test_open_members(self):
        self.assertEqual(categorize_new_member([(45, 10.0), (40, 6.0)]), ["Open", "Open"])

    # 測試混合成員的情況
    def test_mixed_members(self):
        self.assertEqual(categorize_new_member([(58, 8.5), (80, 6.0), (40, 7.0)]), ["Senior", "Open", "Open"])

if __name__ == "__main__":
    unittest.main()