# problem: https://leetcode.com/problems/valid-anagram/
# - TIME: O(n+m), where n length of s, and m is the length of t
# - SPACE: O(n+m)
#   - optimal solution utilziing a hashmap to store both s and t's characters and occurences of each character. Anagrams
#     will have equal dictionaries at the end.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        dictS , dictT= dict(), dict()
        for i in range(len(s)):                     # assuming s and t are the same length
            dictS[s[i]] = 1 + dictS.get(s[i], 0)    # store both s and t in dictionaries
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        
        if dictT == dictS: return True              # compare if their dictionaries are the same. True if yes, False if no.
        return False