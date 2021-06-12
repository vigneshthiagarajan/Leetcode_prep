class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        req = -1
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum_of_two = nums[i] + nums[j]
                if(sum_of_two > req and sum_of_two < k):
                    req = sum_of_two
        return req
