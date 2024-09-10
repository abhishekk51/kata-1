import re
from typing import List, Tuple


class StringCalculator:

    @staticmethod
    def extract_delimeter_and_number(func):
        def wrapper(self, numbers, *args, **kwargs):
            if not numbers:
                return 0

            delimeters, processed_numbers = StringCalculator._extract_delimiter_and_numbers(numbers)

            num_list = StringCalculator._convert_to_numbers(processed_numbers, delimeters)
            return func(self, num_list, *args, **kwargs)

        return wrapper

    @extract_delimeter_and_number
    def add(self, num_list) -> int:

        self._validate_no_negatives(num_list)
        num_list = self._ignore_large_numbers(num_list)

        return sum(num_list)

    @staticmethod
    def _extract_delimiter_and_numbers(numbers: str) -> Tuple[List[str], str]:
        default_delimiter = [","]
        delimiters = default_delimiter
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter_section = parts[0][2:]

            if delimiter_section.startswith("[") and delimiter_section.endswith("]"):
                delimiters = re.findall(r'\[(.*?)\]', delimiter_section)
            else:
                delimiters = [delimiter_section]

            numbers = parts[1]
        return delimiters, numbers

    @staticmethod
    def _convert_to_numbers(numbers: str, delimiters: List[str]) -> List[int]:
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")
        return list(map(int, numbers.split(",")))

    def _validate_no_negatives(self, num_list: List[int]) -> None:
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    def _ignore_large_numbers(self, num_list: List[int]) -> List[int]:
        return [num for num in num_list if num <= 1000]


