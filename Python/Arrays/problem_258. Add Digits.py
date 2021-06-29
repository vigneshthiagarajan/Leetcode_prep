class Solution:
    def addDigits(self, num: int) -> int:
        digits_list = list(map(int, str(num)))
        sum_digits = sum(digits_list)
        while len(digits_list) > 1:
            digits_list = list(map(int, str(sum_digits)))
            sum_digits = sum(digits_list)
        return sum_digits
