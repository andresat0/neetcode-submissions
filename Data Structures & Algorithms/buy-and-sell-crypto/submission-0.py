class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for l in range(0, n):
            for r in range(l + 1, n):
                profit = prices[r] - prices[l]
                
                if profit > max_profit:
                    max_profit = profit

        return max_profit
