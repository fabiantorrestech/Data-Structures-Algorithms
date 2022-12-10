# problem: https://leetcode.com/problems/roman-to-integer/
# - TIME: O(n), where is the size of input string.
# - SPACE: O(1) - constant memory declared no matter size of input [1-3999]
#   - cleaner simpler approach to this problem using onl 1 hashmap!

class Solution:
    def romanToInt(self, s: str) -> int:
        
        norm = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(len(s)):
            if i+1<len(s) and norm[s[i]] < norm[s[i+1]]:    # special cases have 2 chars AND if its a special case,
                                                            # next Character will be greater than curr char 
                                                            # (ex: X (s[i]) < C (s[i+1]) --> 10 < 100)
                ans-= norm[s[i]]
            else:                                           # if norm[s[i]] >= norm[s[i+1]] and/or i+1 out of bounds
                ans+=norm[s[i]]
                
        return ans