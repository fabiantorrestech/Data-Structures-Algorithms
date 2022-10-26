# problem: https://leetcode.com/problems/isomorphic-strings/
# TIME: O(n)
# SPACE: O(n)
# - utilizes 2 dictionaries (1 per string 's' and 't')
# -  mapping must be 1 to 1 for each character. No character can map to 2 characters in either map!

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dictST, dictTS = {}, {}
        
        for i in range(len(s)):
            
            if ((dictST.get(s[i]) and dictST.get(s[i]) != t[i]) or
                (dictTS.get(t[i]) and dictTS.get(t[i]) != s[i])):   # if char exists both dictionaries and mapping for a given char is not equal to the other
                    return False
            
            dictST[s[i]] = t[i]     # map <k,v> -> <s[i], t[i]>
            dictTS[t[i]] = s[i]     # map <k,v> -> <t[i], s[i]>
            
        return True