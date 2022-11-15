# proiblem:
# - TIME: O(s+p) -- # traverse p once, then traverse s once.
# - SPACE: O(p) -- two dicts, both the size of p.
# - optimal approach with 1 pass on s and p, updating dictionaries on the fly.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        dictP, dictS = dict(), dict()
        
        for i in range(len(p)):
            dictP[p[i]] = 1 + dictP.get(p[i], 0)
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
        
        
        ans = [0] if dictS == dictP else []
        l, r = 0, len(p)
        
        for r in range(len(p), len(s)):          # *** (WINDOW SIZE IS ACTUALLY len(p)+1 but len(dictS) == len(p)!!! )
            
            dictS[s[r]] = 1 + dictS.get(s[r], 0) # add in occurence of rightmost char of window in dictS
            dictS[s[l]] -= 1                     # delete occurence of leftmost char of window in dictS
            
            if dictS[s[l]] == 0:                 # if occurences of s[l] in dictS == 0, remove it from dictS
                dictS.pop(s[l])
            
            l+=1                                 # shrink window from left-side (window size is now len(p))

            if dictS == dictP:                   # add idx(l) if dictS == dictP
                ans.append(l)
        
        return ans
            
        
        