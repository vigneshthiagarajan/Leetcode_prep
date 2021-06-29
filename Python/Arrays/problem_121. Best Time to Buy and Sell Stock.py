class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        # max_profit = 0
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if(profit > max_profit):
        #             max_profit = profit
        # return max_profit

        # Optimized in one pass
        min_element_so_far = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_element_so_far:
                min_element_so_far = prices[i]
            else:
                if prices[i] - min_element_so_far > max_profit:
                    max_profit = prices[i] - min_element_so_far
        return max_profit
