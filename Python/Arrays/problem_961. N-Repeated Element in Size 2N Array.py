class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     print(i)
        #     if(nums[i]==nums[i+1]):
        #         return nums[i]
        # return 0

        # Without sort
        counts = collections.Counter(nums)
        for i in counts:
            if counts[i] > 1:
                return i
        return 0
