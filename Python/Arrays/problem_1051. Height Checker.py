class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        num_indices_mismatch = 0
        expected_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected_heights[i]:
                num_indices_mismatch += 1
        return num_indices_mismatch
