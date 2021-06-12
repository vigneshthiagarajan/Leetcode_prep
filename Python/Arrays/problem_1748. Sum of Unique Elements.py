class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        sum_unique = 0
        for key, val in counter.items():
            if val == 1:
                sum_unique += key
        return sum_unique
