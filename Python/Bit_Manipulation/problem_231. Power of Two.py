class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Solution 1 : keep rightmost 1 bit
        # if n == 0:
        #     return False
        # if n == (n & (-n)):
        #     return True
        # return False

        # Solution 2 : Turn off rightmost 1 bit - make it 0
        if n == 0:
            return 0
        return n & (n - 1) == 0
