class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        applied_formula = [a * x * x + b * x + c for x in nums]
        return sorted(applied_formula)
