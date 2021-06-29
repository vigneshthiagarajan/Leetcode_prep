class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Alternate sum of smallest elements, after sorting
        max_sum = sum(sorted(nums)[::2])
        return max_sum
