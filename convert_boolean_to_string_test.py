import unittest
from convert_boolean_to_string import boolean_to_string

class TestConvertBooleanToString(unittest.TestCase):

    def test_boolean_to_string(self):
        # 測試布林值True轉換為字串
        self.assertEqual(boolean_to_string(True), 'True')
        # 測試布林值False轉換為字串
        self.assertEqual(boolean_to_string(False), 'False')

if __name__ == '__main__':
    unittest.main()
