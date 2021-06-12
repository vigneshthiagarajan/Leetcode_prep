class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list_by_parity = self.getEven(A) + self.getOdd(A)
        return list_by_parity

    def getEven(self, A):
        return [i for i in A if i % 2 == 0]

    def getOdd(self, A):
        return [i for i in A if i % 2 == 1]
