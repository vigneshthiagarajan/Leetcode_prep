class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_number = min(nums)
        sum_digits = 0
        for i in str(min_number):
            sum_digits += int(i)
        if(sum_digits % 2 == 1):
            return 0
        return 1
        