class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dict = {}
        for i in range(len(nums)):
            if(nums[i] != 0):
                self.nums_dict[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for key, val in self.nums_dict.items():
            if(key in vec.nums_dict):
                dot_product += val * vec.nums_dict[key]
        return dot_product
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)