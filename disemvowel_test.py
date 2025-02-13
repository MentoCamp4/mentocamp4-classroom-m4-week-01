import unittest
from disemvowel import disemvowel

class TestDisemvowel(unittest.TestCase):

    def test_disemvowel_1(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

    def test_disemvowel_2(self):
        self.assertEqual(disemvowel("Hello World"), "Hll Wrld")

    def test_disemvowel_3(self):
        self.assertEqual(disemvowel("AEIOUaeiou"), "")

if __name__ == '__main__':
    unittest.main()
