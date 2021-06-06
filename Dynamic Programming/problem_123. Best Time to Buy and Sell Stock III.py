# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         if not prices:
#             return 0

#         left_min = prices[0]
#         right_max = prices[-1]

#         # Double way dynamic programming

#         left_profits = [0 for i in range(len(prices))]
#         right_profits = [0 for i in range(len(prices) + 1)]

#         for i in range(1, len(prices)):
#             left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
#             left_min = min(left_min, prices[i])

#         for j in range(1, len(prices)):
#             length = len(prices)

#             right = length - j
#             right_profits[right] = max(
#                 right_profits[right + 1], right_max - prices[right])
#             right_max = max(right_max, prices[right])

#         max_profit = 0
#         for i in range(0, len(prices)):
#             max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

#         return max_profit

# Replace two for loops with single for loop
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        # Double way dynamic programming

        left_profits = [0 for i in range(len(prices))]
        right_profits = [0 for i in range(len(prices) + 1)]

        length = len(prices)
        for i in range(1, len(prices)):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

            right = length - i
            right_profits[right] = max(
                right_profits[right + 1], right_max - prices[right])
            right_max = max(right_max, prices[right])

        max_profit = 0
        for i in range(0, len(prices)):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit
