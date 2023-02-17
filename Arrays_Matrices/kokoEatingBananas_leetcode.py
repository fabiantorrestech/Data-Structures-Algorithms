# problem: https://leetcode.com/problems/koko-eating-bananas/
#  - TIME: O(log(max(piles) * n)), where n=number of all elements in 'piles'
# - SPACE: O(1)
#   - optimal solution implementing a binary search from [1, max(piles)]. 


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles) # binary search, where mid = # bananas that can be eaten per hour. range = [1, biggestPile]
        k = 0
        
        while left <= right:
            mid = (right-left)//2 + left    # given pace -- amount of bananas per hour to try to eat all piles of bananas in <= 'h' hours. 
            tempH = 0                       # temp variable to keep track of how many hours takes to eat at given pace (mid)
            
            for pile in piles:              # try eating all piles at given pace (mid)
                tempH+=math.ceil(pile/mid)  # - we use ceil because:
                                            #   + if we eat less bananas than we originally planned per hour, still takes 1 hour.
                                            #   + if we eat MORE bananas than we originally planned per hour, we just take extra hours.
            
            if tempH > h:                   # would take too long, need to eat more bananas in 1 hour, 
                left = mid + 1
            else:                           # too generous, we can eat less bananas in 1 hour to hit target.
                k = mid
                right = mid - 1
        
        return k