class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num == x:
                return pivot
            elif num > x:
                right = pivot - 1
            else:
                left = pivot + 1

        return right
