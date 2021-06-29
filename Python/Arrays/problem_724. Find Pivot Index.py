class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return -1

        left_sum = 0
        right_sum = sum(nums)

        for i in range(0, len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i

        return -1
