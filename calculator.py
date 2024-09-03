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
        num_list = map(int, numbers.split(delimiter))
        return sum(num_list)
