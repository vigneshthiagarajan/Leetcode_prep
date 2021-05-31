class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for i in range(m)]
        oddCount = 0
        # O(n)
        for index in indices:
            for i in range(0, n):
                matrix[index[0]][i] += 1
            for j in range(0, m):
                matrix[j][index[1]] += 1

        for i in matrix:
            for j in i:
                if j % 2 == 1:
                    oddCount += 1
        return oddCount





