#problem: https://leetcode.com/problems/sqrtx/
# - CANNOT use built in functionality to find sqrt or raise to a power.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        
        while left <= right:
            mid = (right-left)//2 + left
            midSqrd = mid * mid
            
            if midSqrd == x or ((mid+1)*(mid+1) > x and midSqrd < x):   # or case corresponds to case where given x has
                                                                        # no perfect sqrt, so we round down the answer. 
                return mid
            elif midSqrd > x:
                right = mid-1
            elif midSqrd < x:
                left = mid+1