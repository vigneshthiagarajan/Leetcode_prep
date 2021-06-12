class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        SumAlice, SumBob = sum(aliceSizes), sum(bobSizes)
        setBob = set(bobSizes)
        for i in aliceSizes:
            if i + (SumBob-SumAlice)/2 in setBob:
                return [i, i + (SumBob-SumAlice)/2]