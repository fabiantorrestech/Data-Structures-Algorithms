class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        totalProfit, currProfit = 0, 0
        
        for day in range(len(prices)):
            for futureDay in range(day, len(prices)):
                currProfit = max(currProfit, prices[futureDay]-prices[day])
            totalProfit = max(totalProfit, currProfit)
        
        return totalProfit