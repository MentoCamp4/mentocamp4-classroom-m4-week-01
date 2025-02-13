import unittest
from keep_hydrated import litres

class TestKeepHydrated(unittest.TestCase):

    def test_litres(self):
        # 測試不同的時間輸入
        self.assertEqual(litres(2), 1)
        self.assertEqual(litres(3.5), 1)
        self.assertEqual(litres(5), 2)
        self.assertEqual(litres(0.8), 0)
        self.assertEqual(litres(12.3), 6)

if __name__ == '__main__':
    unittest.main()