class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n^2)
        #         max_subarray = -math.inf
        #         for i in range(len(nums)):
        #             current_subarray = 0
        #             for j in range(i, len(nums)):
        #                 current_subarray += nums[j]
        #                 max_subarray = max(max_subarray, current_subarray)

        #         return max_subarray
        current_sub = nums[0]
        max_sub = nums[0]

        for num in nums[1:]:
            current_sub = max(current_sub + num, num)
            max_sub = max(max_sub, current_sub)
        return max_sub
