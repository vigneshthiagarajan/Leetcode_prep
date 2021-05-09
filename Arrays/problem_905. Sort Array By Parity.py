class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return self.getEven(A) + self.getOdd(A)

    def getEven(self, A):
        return [i for i in A if i % 2 == 0]

    def getOdd(self, A):
        return [i for i in A if i % 2 == 1]
