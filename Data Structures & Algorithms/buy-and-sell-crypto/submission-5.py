class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                # Edge case: need at least 2 prices to trade
        if len(prices) < 2:
            return 0
        
        min_price = float("inf")  # Start with first price
        max_profit = 0
        
        for price in prices:
            # Update minimum price if current is lower
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at current price
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit