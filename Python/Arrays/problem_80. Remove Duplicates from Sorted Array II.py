class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        if len(nums) == 1:
            return 1
        i = 1
        while i < (len(nums) - 1):
            if nums[i - 1] == nums[i] and nums[i] == nums[i + 1]:
                print(nums[i])
                nums.pop(i)
                i -= 1
            i += 1

        return len(nums)

        # i = 1
        # counter = 1
        # while i < (len(nums)):
        #     if(nums[i-1] == nums[i]):
        #         counter += 1
        #         if(nums[i-1] == nums[i] and counter > 2):
        #             nums.pop(i)
        #             i -= 1
        #     else:
        #         counter = 1
        #     i += 1
        #
        # return len(nums)
