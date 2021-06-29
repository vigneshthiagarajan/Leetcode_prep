class Solution:
    # def nthUglyNumber(self, n: int) -> int:
    #     brute force
    #         uglies = set([1, 2, 3, 5])
    #         length = 3
    #         if (n >= 3):
    #             while(length < n*n):
    #                 for i in list(uglies):
    #                     for j in [2,3,5]:
    #                         to_add = i*j
    #                         if to_add not in uglies:
    #                             uglies.add(to_add)
    #                             length += 1
    #         uglies_list = sorted(list(uglies))
    #         print(uglies_list)
    #         print(n)
    #         return uglies_list[n-1]

    def nthUglyNumber(self, n: int) -> int:
        num = [0] * n
        num[0] = 1
        i2, i3, i5 = 0, 0, 0
        mul_2 = 2
        mul_3 = 3
        mul_5 = 5
        for i in range(1, n):
            print(num)
            num[i] = min(mul_2, mul_3, mul_5)
            if num[i] == mul_2:
                i2 += 1
                mul_2 = num[i2] * 2
            if num[i] == mul_3:
                i3 += 1
                mul_3 = num[i3] * 3
            if num[i] == mul_5:
                i5 += 1
                mul_5 = num[i5] * 5
        return num[-1]
