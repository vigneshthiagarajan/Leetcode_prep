class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_num(n):
            sum_squares = 0
            while (n > 0):
                n, digit = divmod(n, 10)
                sum_squares += digit ** 2
            return sum_squares

        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next_num(n)
            if n in visited:
                return False

        return True




