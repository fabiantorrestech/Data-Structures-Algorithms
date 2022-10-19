#problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# - method 1: utilizing a set() to keep track of all repeatedCharacters
#       + until we remove the repeated occurence of character, it will still exist in the set.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = set()
        left, longestSubstr = 0, 0
        
        for right in range(len(s)):
            while s[right] in seenChars:    # we've detected repeated character thats same as right ptr
                seenChars.remove(s[left])   # - delete the duplicate from set. it will stil appear in set
                                            #   until duplicate has been deleted.
                left += 1
            
            seenChars.add(s[right])         # add unseen character to set
            windowSize = (right-left)+1
            longestSubstr = max(longestSubstr, windowSize)
            
        return longestSubstr
        