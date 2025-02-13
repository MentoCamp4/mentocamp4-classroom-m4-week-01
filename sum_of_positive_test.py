import unittest
from sum_of_positive import positive_sum

class TestPositiveSum(unittest.TestCase):

    def test_positive_sum(self):
        # 測試列表包含正數的情況
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        # 測試列表包含正數和負數的情況
        self.assertEqual(positive_sum([1, -2, 3, -4, 5]), 9)
        # 測試空列表的情況
        self.assertEqual(positive_sum([]), 0)
        # 測試列表只包含負數的情況
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)
        # 測試列表只包含0的情況
        self.assertEqual(positive_sum([0, 0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
