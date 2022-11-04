# problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# - TIME:  O(n)
# - SPACE: O(1) - chars list, which will not scale with input at all.
    # - List/Array solution. (optimal)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = [0] * 26                    # use array[26] for keeping char # of occurences of all alpha-characters.
                                            # a=0, b=1, c=2, ... , x=23, y=24, z=25
        
        for i in range(len(s)):             # traverse string once: use ascii value to store char occurences in index corresponding to letter
            chars[ord(s[i])-ord('a')] +=1
        
        for i in range(len(s)):             # traverse string again: use chars # of occurences. first one to have only 1 is firstUniqueCharacter. return i.
            if chars[ord(s[i])-ord('a')] == 1:
                return i
        
        return -1                           # if no char # of occurences = 1, it doesn't exist.
            
        
        