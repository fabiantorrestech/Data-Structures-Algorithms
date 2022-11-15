# problem: https://leetcode.com/problems/isomorphic-strings/
# TIME: O(n)
# SPACE: O(n)
# - utilizes 2 dictionaries (1 per string 's' and 't')
# -  mapping must be 1 to 1 for each character. No character can map to 2 characters in either map!

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dictS, dictT = dict(), dict()                               # dictS = for each letter in S, map T's letters
                                                                    # dictT = for each letter in T, map S's letters
        
        for i in range(len(s)):
            sChar, tChar = s[i], t[i] 
            
            if ((sChar in dictS and dictS[sChar] != tChar) or      # there is a mapping for sChar in dictS AND mapping for sChar is not tChar
                (tChar in dictT and dictT[tChar] != sChar)):       # there is a mapping for tChar in dictT AND mapping for tChar is not sChar
                return False
            
            dictS[sChar] = tChar                                    # map t's letters to S (if a mapping is doubly mapped/overwritten, it will take on new value)
            dictT[tChar] = sChar                                    # map S's letters to T
        
        return True
        