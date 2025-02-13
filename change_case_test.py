import unittest
from change_case import change_case

class TestChangeCase(unittest.TestCase):

    def test_upper_case(self):
        self.assertEqual(change_case("Hello World", "upper"), "HELLO WORLD")
        self.assertEqual(change_case("HeLLo WoRLD", "upper"), "HELLO WORLD")

    def test_lower_case(self):
        self.assertEqual(change_case("HeLLo WoRLD", "lower"), "hello world")
        self.assertEqual(change_case("PYTHON IS FUN!", "lower"), "python is fun!")

if __name__ == '__main__':
    unittest.main()
