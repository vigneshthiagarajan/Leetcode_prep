class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Simple sort
        squared = [i * i for i in nums]
        squared.sort()
        return squared


