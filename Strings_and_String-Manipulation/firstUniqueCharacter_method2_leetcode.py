# problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# - TIME:  O(n)
# - SPACE: O(1) - chars list, which will not scale with input at all.
    # - Hashmap solution. (optimal)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = dict()              # declare a dictionary to keep occurences of characters.
        
        for i in range(len(s)):     # loop through string 's' once": count occurences of 's's characters
            if not chars.get(s[i]):
                chars[s[i]] = 1
            else:
                chars[s[i]] +=1
        
        for i in range(len(s)):     # loop though 's' again: check each of 's's character's occurences -- when we find that a character's occurences == 1, return idx.   
            if chars[s[i]] == 1:
                return i
        
        return -1                   # if no char # of occurences = 1, it doesn't exist.