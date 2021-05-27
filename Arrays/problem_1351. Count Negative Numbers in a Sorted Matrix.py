class Solution:
    # O(n^2)
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_count = 0
        if (len(grid) == 0):
            return 0
        for i in range(0, len(grid)):
            for j in range(len(grid[0]) - 1, -1, -1):
                if (grid[i][j] < 0):
                    negative_count += 1
                else:
                    break
        return negative_count
