# problem: https://leetcode.com/problems/permutation-in-string/
# - approach with hashmap with lowercase letters.
# incomplete !!!

import string

class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        zeroes = [0] * 26
        dictS1 = dict(zip(string.ascii_lowercase, zeroes))  # create a map of 26 characters and occurences for S1 & S2
        dictS2 = dict(zip(string.ascii_lowercase, zeroes))
        
        matches = 0
        countedMatches = False
        left, right = 0, len(s1)-1          # designate boundaries for sliding window (permutation must be of size 's1')
        
        for i in range(len(s1)):            # count all characters in s1
            dictS1[s1[i]] += 1
        
        for i in range(len(s1)):            # count all characters in s2
            dictS2[s2[i]] += 1
        
        print(dictS2)
            
        
        while right < len(s2):              # count mismatches 
            
            print("comparing ",s1, " to ", s2[left:right+1])
            
            if not countedMatches:
                for i in range(len(dictS1)):        # count all the matches we have between S1 and S2 in first substring.
                    currChar = chr(ord('a')+i)
                    if dictS1[currChar] == dictS2[currChar]:
                        matches+=1
                    else:
                        matches-=1
                print(matches)
                countedMatches = True

            if matches == 26: return True
            
            # recount changes to matches
            if s1[right]
            
            left+=1
            right+=1
        

            
            
        return False