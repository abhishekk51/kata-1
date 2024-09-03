import unittest
from calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number_returns_the_number_itself(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1"), 1)


if __name__ == '__main__':
    unittest.main()
