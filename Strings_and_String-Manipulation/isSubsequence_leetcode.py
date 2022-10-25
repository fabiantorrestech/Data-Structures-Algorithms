# problem: https://leetcode.com/problems/is-subsequence/
# TIME: O(n)
# SPACE: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        p1, p2 = 0, 0   # s[p1], t[p2]
        
        while (p1 <= len(s)-1 ) and (p2 <= len(t)-1):
            if s[p1] == t[p2]:
                p1+=1
            p2 += 1
                
        if p1 == len(s):    # if we have finished traversing s, then it exists in t as a subsequence.
            return True
        
        return False