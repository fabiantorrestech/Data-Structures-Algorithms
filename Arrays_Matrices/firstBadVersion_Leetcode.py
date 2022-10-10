# problem: https://leetcode.com/problems/first-bad-version/?envType=study-plan&id=algorithm-i

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n
        
        while left < right:
            mid = ((right-left)//2) + left
            
            if isBadVersion(mid): # discard right half of list. check left for more bad versions.
                right = mid       # - SAVE mid bc it may be 1stBadVersion!
            else:
                left = mid+1      # discard left half of list. haven't yet found a bad version.
                
        return right              # return left OR right. both correct. (for lists of size 1)   
                
        