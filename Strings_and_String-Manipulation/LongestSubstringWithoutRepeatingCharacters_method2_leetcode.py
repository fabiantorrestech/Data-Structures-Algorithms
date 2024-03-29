# problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# - method 2 uses dict() to keep exact count of all occurences of characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right, maxSubstr = 0, 0, 0
        seenChars = dict()
        
        while right < len(s):
            
            if seenChars.get(s[right]) == None: # add occurences of letters into dictionary
                seenChars[s[right]] = 1
            else:
                seenChars[s[right]]+=1
            
            while seenChars[s[right]] > 1: # get rid of duplicates
                seenChars[s[left]]-=1
                left+=1
            
            windowSize = right-left + 1
            maxSubstr = max(maxSubstr, windowSize)
            
            right += 1

        return maxSubstr