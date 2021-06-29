class Solution:
    # O(n^n) - recursion
    #     def maxProfit(self, prices: List[int]) -> int:
    #         return self.calculate_all(prices, 0)

    #     def calculate_all(self, prices, start):
    #         if(start >= len(prices)):
    #             return 0
    #         max_sum = 0
    #         for i in range(start, len(prices)):
    #             max_profit = 0
    #             for j in range(i+1, len(prices)):
    #                 profit = 0
    #                 if(prices[i] < prices[j]):
    #                     profit = self.calculate_all(prices, j+1) + prices[j] - prices[i]
    #                     if(profit > max_profit):
    #                         max_profit = profit
    #             if(max_profit > max_sum):
    #                 max_sum = max_profit
    #         return max_sum

    # def maxProfit(self, prices: List[int]) -> int:
    #     # One pass using simple math, shown by graph
    #     class Solution:
    # O(n^n) - recursion
    #     def maxProfit(self, prices: List[int]) -> int:
    #         return self.calculate_all(prices, 0)

    #     def calculate_all(self, prices, start):
    #         if(start >= len(prices)):
    #             return 0
    #         max_sum = 0
    #         for i in range(start, len(prices)):
    #             max_profit = 0
    #             for j in range(i+1, len(prices)):
    #                 profit = 0
    #                 if(prices[i] < prices[j]):
    #                     profit = self.calculate_all(prices, j+1) + prices[j] - prices[i]
    #                     if(profit > max_profit):
    #                         max_profit = profit
    #             if(max_profit > max_sum):
    #                 max_sum = max_profit
    #         return max_sum

    def maxProfit(self, prices: List[int]) -> int:
        # One pass using simple greedy rule, shown by graph
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit
