import re
from typing import List, Tuple


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter, numbers = self._extract_delimiter_and_numbers(numbers)
        num_list = self._convert_to_numbers(numbers, delimiter)

        self._validate_no_negatives(num_list)
        num_list = self._ignore_large_numbers(num_list)

        return sum(num_list)

    def _extract_delimiter_and_numbers(self, numbers: str) -> Tuple[List[str], str]:
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

    def _convert_to_numbers(self, numbers: str, delimiters: List[str]) -> List[int]:
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
