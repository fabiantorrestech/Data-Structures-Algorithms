# problem: https://leetcode.com/problems/valid-palindrome/
# - TIME: O(2n) -> O(n), where n is the number of characters in the input string 's' 
# - SPACE: O(n)
#   - pythonic way to compare a string if it is the same way reverse as forwards (slices operator).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #create a new string since python strings are immutable
        temp = []
        for i in range(len(s)):
            if s[i].isalnum():
                temp.append(s[i].lower())
        
        # pythonic way to compare 'temp' and reversed 'temp', using slice operator.
        return True if temp == temp[::-1] else False 
            