class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        sumHeight = 0
        for i in gain:
            sumHeight += i
            if sumHeight > maxHeight:
                maxHeight = sumHeight
        return maxHeight
