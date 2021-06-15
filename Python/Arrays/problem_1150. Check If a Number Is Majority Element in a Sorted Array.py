class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        before_idx = 0
        after_idx = len(nums) - 1
        while(nums[before_idx] != target and before_idx <= len(nums) - 2):
            before_idx += 1
        while(nums[after_idx] != target and after_idx >= 0):
            after_idx -= 1
        
        if(after_idx - before_idx >= math.floor(len(nums)/2)):
            return True
        return False

    # Binary search right most - left most

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return bisect_right(nums, target)-bisect_left(nums, target) > len(nums)//2
