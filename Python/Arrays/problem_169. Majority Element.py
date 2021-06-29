class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counts = collections.Counter(nums)
        n = len(nums)
        for key, value in nums_counts.items():
            if value > math.floor(n / 2):
                return key
        return -1
