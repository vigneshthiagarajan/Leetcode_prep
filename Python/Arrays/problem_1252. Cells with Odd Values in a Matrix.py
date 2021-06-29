class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        #         matrix = [[0]*n for i in range(m)]
        #         oddCount = 0
        #         # O(n)
        #         for index in indices:
        #             for i in range(0, n):
        #                 matrix[index[0]][i]+=1
        #             for j in range(0, m):
        #                 matrix[j][index[1]] +=1

        #         for i in matrix:
        #             for j in i:
        #                 if j%2 == 1:
        #                     oddCount += 1
        #         return oddCount

        # Faster

        counts = 0

        rows = [0 for i in range(m)]
        columns = [0 for j in range(n)]

        for [row, col] in indices:
            rows[row] += 1
            columns[col] += 1

        for i in rows:
            for j in columns:
                if (i + j) % 2 == 1:
                    counts += 1

        return counts
