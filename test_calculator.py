import unittest
from calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number_returns_the_number_itself(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1"), 1)

    def test_two_numbers_comma_delimited(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2"), 3)

    def test_multiple_numbers_comma_delimited(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3,4"), 10)

    def test_newlines_between_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1\n2,3"), 6)

    def test_different_delimiters(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)


if __name__ == '__main__':
    unittest.main()
