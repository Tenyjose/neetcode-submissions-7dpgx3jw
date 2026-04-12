"""
PROBLEM UNDERSTANDING

Given an array of stock prices where prices[i] is the price on day i,
find the maximum profit from buying on one day and selling on a later day.

If no profit is possible, return 0.

Input: Array of integers (stock prices)
Output: Integer (maximum profit achievable)

Constraints:
- Must buy before selling (can't sell before buying)
- Can only do one transaction (one buy + one sell)
- If no profit possible, return 0

Edge cases: Prices only decrease, single price, all same prices
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        APPROACH
        
        Track the minimum price seen so far and maximum profit.
        
        Strategy:
        1. Keep track of minimum price encountered
        2. For each price, calculate profit if we sell today
           (current price - minimum price seen so far)
        3. Update maximum profit if current profit is better
        
        Key insight:
        To maximize profit, we want to buy at lowest price
        and sell at highest price AFTER that low point.
        
        We don't need to track when to buy/sell, just the profit amount.
        
        Time Complexity: O(n) - single pass through prices
        Space Complexity: O(1) - only two variables
        """
        
        # Edge case: need at least 2 prices to trade
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]  # Start with first price
        max_profit = 0
        
        for price in prices:
            # Update minimum price if current is lower
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at current price
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit

"""
REASONING

Single-pass algorithm tracks minimum price and calculates profit at each step.

Example: prices = [7, 1, 5, 3, 6, 4]

Day 0: price=7
  min_price = min(7, 7) = 7
  profit = 7 - 7 = 0
  max_profit = 0

Day 1: price=1
  min_price = min(7, 1) = 1  (new minimum!)
  profit = 1 - 1 = 0
  max_profit = 0

Day 2: price=5
  min_price = min(1, 5) = 1
  profit = 5 - 1 = 4
  max_profit = 4  (best so far!)

Day 3: price=3
  min_price = min(1, 3) = 1
  profit = 3 - 1 = 2
  max_profit = 4

Day 4: price=6
  min_price = min(1, 6) = 1
  profit = 6 - 1 = 5
  max_profit = 5  (new best! Buy at 1, sell at 6)

Day 5: price=4
  min_price = min(1, 4) = 1
  profit = 4 - 1 = 3
  max_profit = 5

Result: 5 (buy at 1, sell at 6) ✓

Why this works:
By tracking minimum price, we always know the best buy point
seen so far. Each day we calculate profit if we sell today.

Edge cases handled:
- Decreasing prices [7,6,5,4,3]: max_profit stays 0 ✓
- Single price [5]: return 0 ✓
- All same [3,3,3,3]: max_profit = 0 ✓

Alternative: Brute force checking all pairs would be O(n²), rejected.
"""