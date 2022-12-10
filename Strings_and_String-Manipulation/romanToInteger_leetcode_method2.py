# problem: https://leetcode.com/problems/roman-to-integer/
# - TIME: O(n), where is the size of input string.
# - SPACE: O(1) - constant memory declared no matter size of input [1-3999]
#   - initial approach to solving this problem, correct, but somwehat messy solution.


class Solution:
    def romanToInt(self, s: str) -> int:
        
        norm = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        special = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        edgeCases = set(['V', 'X', 'L', 'C', 'D', 'M'])
        
        ans = 0
        i = len(s)-1
        while i >= 0:                                # traverse the string backwards and construct answer from smaller
                                                     # to larger numbers.
            if s[i] in edgeCases:
                if i-1>=0 and s[i-1:i+1] in special: # check special (must be two characters, in string's bounds)
                    specialNum = s[i-1:i+1] 
                    ans+=special[specialNum]
                    i-=1                             # decrement by two in this loop-iteration since we covered two-character special case
                                                     # (ex: XC, IV, etc... )

                else:                                # just a one or a normal case. it is a one-character input not included in special cases!
                    ans+=norm[s[i]]
            
            else:                                    # just a one or a normal case. it is a one-character input not included in special cases!
                ans+=norm[s[i]]
            
            i-=1
                    
        return ans
        