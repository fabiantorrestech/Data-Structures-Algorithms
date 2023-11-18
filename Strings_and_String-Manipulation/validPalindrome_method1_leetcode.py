# problem: https://leetcode.com/problems/valid-palindrome/
# - TIME: O(n)
# - SPACE: O(1)
#   + the most optimal solution. 1 pass which is O(n) time at worst. 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        while left < right:
            while left<right and not s[left].isalpha() and not s[left].isnumeric():
                left+=1
            while left<right and not s[right].isalpha() and not s[right].isnumeric():
                right-=1
            
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
            
        return True