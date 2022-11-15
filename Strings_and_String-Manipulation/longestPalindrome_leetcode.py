# problem: https://leetcode.com/problems/longest-palindrome/
# - TIME: O(n)
# - SPACE: O(52) - worst case, we have to make a dict entry for each upper and lower case letter (26*2)
# - Space

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dictS = dict()
        for i in range(len(s)):                      # count occurences of all characters
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            
        longestP = 0
        for key in dictS:
            longestP += dictS[key] // 2 * 2          # extracts the highest even number that goes into the value. (for dictS[key].)
            
            if longestP%2== 0 and dictS[key]%2 == 1: # if longestP is even and curr 'dictS[key]' is odd, count it ONCE 
                                                     # (since now longestP will only count even numbers, it will never be even again after +=1). 
                longestP+=1
            
        return longestP
        