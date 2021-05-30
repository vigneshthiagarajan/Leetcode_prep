class Solution:
    def maximum69Number (self, num: int) -> int:
        num_string = str(num)
        num_string = num_string.replace("6", "9", 1)
        return int(num_string)