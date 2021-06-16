class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        # # Two pass
        # check = (all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)))
        # return check
    
        # One pass
        increasing = True
        decreasing = True
        
        for i in range(len(nums)-1):
            if(nums[i+1] < nums[i]):
                increasing = False
            if(nums[i+1] > nums[i]):
                decreasing = False
        return decreasing or increasing
                
        
            
            
            
            
        