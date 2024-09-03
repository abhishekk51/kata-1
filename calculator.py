import re


class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        numbers = numbers.replace("\n", delimiter)
        num_list = list(map(int, numbers.split(delimiter)))

        negatives = [num for num in num_list if num < 0]
        if negatives:
            # We can add the error string as constant somewhere to make it modular
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        num_list = [num for num in num_list if num <= 1000]
        return sum(num_list)
