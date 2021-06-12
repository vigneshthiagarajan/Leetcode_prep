class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counts = collections.Counter(A)
        singles = []
        for i in counts:
            if counts[i] == 1:
                singles.append(i)
        singles.sort(reverse=True)
        if singles:
            return singles[0]
        return -1
