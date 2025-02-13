import unittest
from calculate_average import calculate_average

class TestCalculateAverage(unittest.TestCase):

    def test_calculate_average_1(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_calculate_average_2(self):
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30.0)

    def test_calculate_average_3(self):
        self.assertEqual(calculate_average([3, 7, 21, 13]), 11.0)

if __name__ == '__main__':
    unittest.main()
