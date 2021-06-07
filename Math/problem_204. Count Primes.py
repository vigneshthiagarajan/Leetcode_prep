class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        dict_non_prime = set()

        for num in range(2, int(sqrt(n)) + 1):
            for multi in range(num*num, n, num):
                if multi not in dict_non_prime:
                    dict_non_prime.add(multi)

        return n - len(dict_non_prime) - 2
