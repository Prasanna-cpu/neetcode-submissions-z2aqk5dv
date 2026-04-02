class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = float("inf")

        for p in prices:
            min_price = min(p, min_price)
            price_difference = abs(min_price - p)
            max_profit = max(max_profit, price_difference)
        return max_profit