# problem: https://leetcode.com/problems/permutation-in-string/
# - TIME: O(s1+s2)
# - SPACE: O(s1) - dictionaries allocated of size S1 (for both dictS1 and dictS2)
#   - very similar to "Find All Anagrams in String" on leetcode! this is easier version of that! (:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        dictS1, dictS2 = dict(), dict()
        for i in range(len(s1)):                    # count all occurences of first len(s1) # of letters in S1 and S2
            dictS1[s1[i]] = 1 + dictS1.get(s1[i], 0)
            dictS2[s2[i]] = 1 + dictS2.get(s2[i], 0)
        
        if dictS1 == dictS2: return True            # see if theres an anagram before we begin looping.
        
        left, right = 0, len(s1)                             # sliding window algorithm approach...

        while right < len(s2):
            dictS2[s2[right]] = 1 + dictS2.get(s2[right], 0) # add occurence of rightmost char
            dictS2[s2[left]] -= 1                            # decrement occurence of leftmost char
            
            if dictS2[s2[left]] == 0:                        # remove leftmost char from dictS2 if occurrences of leftmost char = 0
                dictS2.pop(s2[left])
            
            left+=1                                          # advance left
            
            if dictS1 == dictS2: return True                 # compare dictS1 and dictS2 -- if anagram detected, return true.
            
            # advance right
            right+=1
        
        
        return False                                # there must not exist an anagram of S1 in S2 if it reaches here.
        
        