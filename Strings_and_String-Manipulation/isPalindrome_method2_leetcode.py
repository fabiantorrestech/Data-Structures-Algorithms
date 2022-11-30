# problem: https://leetcode.com/problems/valid-palindrome/
# - TIME: O(2n) -> O(n), where n is the number of characters in the input string 's' 
# - SPACE: O(n)
#   - compared left and right temp string one by one characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #create a new string since python strings are immutable
        temp = []
        for i in range(len(s)):
            if s[i].isalpha():
                temp.append(s[i].lower())
                
        # compare from left to right that the new string is the exact same.
        left, right = 0, len(temp)-1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left+=1
            right-=1
        return True
            