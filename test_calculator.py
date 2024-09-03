import unittest


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()


if __name__ == '__main__':
    unittest.main()
