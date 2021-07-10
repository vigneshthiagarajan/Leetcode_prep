class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        if len(nums) == 0:
            return 0
        while low <= high:
            pivot = int((low + high) / 2)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                low = low + 1
            else:
                high = high - 1
        return low
