class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        # Two pass
        check = (all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)))
        return check
    
        
            
            
            
            
        