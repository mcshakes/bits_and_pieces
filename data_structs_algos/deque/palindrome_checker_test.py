import unittest
from palindrome_checker import pal_checker


class PalCheckerTest(unittest.TestCase):

    def test_pal_checker(self):
        self.assertTrue(pal_checker("radar"), True)

    def test_pal_checker(self):
        self.assertTrue(pal_checker("poop"))

    def test_pal_checker(self):
        self.assertFalse(pal_checker("gambit"))


if __name__ == '__main__':
    unittest.main()
