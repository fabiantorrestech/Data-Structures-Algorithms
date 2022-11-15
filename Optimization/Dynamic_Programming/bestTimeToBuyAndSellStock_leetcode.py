# problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# - TIME: O(n)
# - SPACE: O(1)
# 2 pointer solution. (greedy & dynamic programming)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2: return 0
        
        l, r = 0, 1                             # l = (buy) price bought at, r = (sell) price sold at
        maxProfit = 0
        while r < len(prices):
            currProfit = prices[r]-prices[l]        # currProfit = sell - buy
            maxProfit = max(maxProfit, currProfit)  # overwrite maxProfit if currProfit is greater
            if prices[r]<prices[l]:                 # set l = r, bc we found a low price to buy at.
                l=r
            r+=1
        
        return maxProfit