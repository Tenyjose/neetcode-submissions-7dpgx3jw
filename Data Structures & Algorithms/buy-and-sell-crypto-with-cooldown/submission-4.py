class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        holding  = float('-inf')
        sold     = 0
        cooldown = 0

        for price in prices:
            prev_holding = holding
            prev_sold = sold
            prev_cooldown = cooldown

            holding = max(prev_cooldown-price,prev_holding)
            sold = prev_holding+price
            cooldown = max(prev_sold,prev_cooldown)

        return max(sold,cooldown)
            



"""
Given Prices = [1,3,4,0,4]

"""