import unittest
from calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)


if __name__ == '__main__':
    unittest.main()
