# problem: https://leetcode.com/problems/first-bad-version/?envType=study-plan&id=algorithm-i

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n
        firstBad = -1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if isBadVersion(mid) == True:
                firstBad = mid              # Keep track of earliest BadVersion Tracked so far..
                right = mid-1               # reduce target list of binary search to left half (excluding mid)
            else:
                left = mid+1                # reduce target list of binary search to right half (excluding mid)
                
        return firstBad  
                
        