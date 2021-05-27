class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = collections.Counter(deck).values()
        return math.gcd(*counts) >= 2


