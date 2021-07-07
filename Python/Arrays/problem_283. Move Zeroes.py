class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0
        for pointer2 in range(len(nums)):
            if(nums[pointer2] != 0):
                temp = nums[pointer1]
                nums[pointer1] = nums[pointer2]
                nums[pointer2] = temp
                pointer1 += 1
