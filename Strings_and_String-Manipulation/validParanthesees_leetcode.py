# problem: https://leetcode.com/problems/valid-parentheses/
# - TIME: O(n), where n is length of string 's'
# - SPACE: O(n) space, at WORST
#   - Optimal solution

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)<2: return False                   # base case: False if len(s)<2
        
        charsDict = { '}': '{', ']':'[', ')':'(' }  # for these characters at s[i], take a look at the stack
        q = deque()        
        for i in range(len(s)):
            if (s[i] in charsDict and len(q)>0
                and charsDict[s[i]] == q[-1]):
                q.pop()
            else:
                q.append(s[i])

        return True if len(q)==0 else False
        