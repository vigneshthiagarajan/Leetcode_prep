class Solution:
    def findComplement(self, num: int) -> int:
        to_do = num
        bit = 1
        while(to_do):
            num = num ^ bit
            bit = bit << 1
            to_do = to_do >> 1
        return num
        