class Solution:
    def generateTheString(self, n: int) -> str:
        filler = ["a", "b", "c"]
        if n == 1:
            return filler[0]
        if n % 2 == 0:
            result = filler[0] * (n - 1) + filler[1]
        else:
            result = filler[0] * (n - 2) + filler[1] + filler[2]
        return result
