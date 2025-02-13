import unittest
from jennys_secret_message import greet

class TestJennysSecretMessage(unittest.TestCase):

    def test_greet_johnny(self):
        self.assertEqual(greet("Johnny"), "Hello, my love!")

    def test_greet_other_names(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet("Tom"), "Hello, Tom!")

if __name__ == '__main__':
    unittest.main()
