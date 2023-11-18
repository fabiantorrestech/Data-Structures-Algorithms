# problem: https://leetcode.com/problems/valid-palindrome/
# - TIME: O(2n) -> O(n)
# - SPACE: O(n)
#   + not the most optimal solution, requires 2 passes and space for another string of <= len(s). 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # cleanse the input string of non-alphanumeric characters
        newS = ""
        for i, letter in enumerate(s):
            if letter.isalpha() or letter.isnumeric():
                newS += letter.lower()
        
        # compare the new string, left to right.
        left, right = 0, len(newS)-1
        while left < right:
            print(newS[left] + " -- " + newS[right])
            if newS[left] != newS[right]:
                return False
            left+=1
            right-=1
        
        return True