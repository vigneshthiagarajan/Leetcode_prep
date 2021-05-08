class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        max_sum = sum(sorted(nums)[::2])
        return max_sum