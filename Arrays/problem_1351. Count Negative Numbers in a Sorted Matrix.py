class Solution:
    #     # O(n^2)
    #     def countNegatives(self, grid: List[List[int]]) -> int:
    #         negative_count = 0
    #         if(len(grid)==0):
    #             return 0
    #         for i in range(0, len(grid)):
    #             for j in range(len(grid[0])-1, -1, -1):
    #                 if(grid[i][j]<0):
    #                     negative_count+=1
    #                 else:
    #                     break
    #         return negative_count

    def countNegatives(self, grid: List[List[int]]) -> int:
        def indexOfNegative(start: int, end: int, row: List[int]) -> int:
            while start <= end:
                mid = start + (end - start) // 2

                if row[mid] < 0:
                    if mid > 0 and row[mid - 1] >= 0 or mid == 0:
                        return mid
                    else:
                        end = mid - 1
                else:
                    start = mid + 1

            return -1

        MAX_ROWS, MAX_COLS, result = len(grid), len(grid[0]), 0

        for i in range(MAX_ROWS):
            index = indexOfNegative(0, MAX_COLS - 1, grid[i])

            if index == -1:
                continue

            result += (MAX_COLS - index) * (MAX_ROWS - i)
            MAX_COLS = index

        return result