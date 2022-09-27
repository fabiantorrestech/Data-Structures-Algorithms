# problem: https://leetcode.com/problems/first-bad-version/?envType=study-plan&id=algorithm-i

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # n = total number of versions.
        # ... so use binary search to solve for the first bad version.
        # - iterative or Recursive BS? iterative by the way it works.
        
        left = 1
        right = n
        while left < right:
            mid = int(left + (right-left)/2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        
        return left
        