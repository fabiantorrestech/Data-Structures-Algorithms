# problem: https://leetcode.com/problems/isomorphic-strings/
# TIME: O(n)
# SPACE: O(n)
# - utilizes 1 map and whether any duplicate values exist for all keys

class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        charMap = {}                            # for mappping <k,v> -> <s[i], t[i]>
        
        for i in range(len(s)):
            sChar = s[i]
            if charMap.get(sChar) == None:
                charMap[sChar] = tChar          # inserting values for keys
                
            elif charMap.get(sChar) != tChar:
                return False                    # if we have an s[i]-> t[i] mapping, it cannot map to 2nd character!

        if not len(charMap.values()) == len(set(charMap.values())): # - check if any keys have duplicate values -- if yes, is not isomorphic
                                                                    # - compare length of map-values to set(map-values). since sets don't count duplicate mappings,
                                                                    #   this will always work to check for doubly-mapped values. 
            return False
        
        return True
        