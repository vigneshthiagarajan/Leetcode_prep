class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        #         # Brute force
        #         req = -1
        #         for i in range(0, len(nums)):
        #             for j in range(i+1, len(nums)):
        #                 sum_of_two = nums[i] + nums[j]
        #                 if(sum_of_two > req and sum_of_two < k):
        #                     req = sum_of_two
        #         return req

        # Two pointers
        nums.sort()
        pointer1 = 0
        pointer2 = len(nums)-1
        ans = -1
        while(pointer1 < pointer2):
            sum_val = nums[pointer1] + nums[pointer2]
            if(sum_val < k):
                if(sum_val > ans):
                    ans = sum_val
                pointer1 += 1
            else:
                pointer2 -= 1
        return ans
