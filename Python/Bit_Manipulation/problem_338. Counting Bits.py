class Solution:
    def countBits(self, n: int) -> List[int]:
        return_array = []
        for i in range(n + 1):
            count = 0
            while i:
                if i & 1:
                    count += 1
                i = i >> 1
            return_array.append(count)
        return return_array
