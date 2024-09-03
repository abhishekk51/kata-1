class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        numbers = numbers.replace("\n", ",")
        num_list = map(int, numbers.split(","))
        return sum(num_list)
