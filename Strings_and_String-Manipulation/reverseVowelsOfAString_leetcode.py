# problem: https://leetcode.com/problems/reverse-vowels-of-a-string/
# - TIME: O(n)
# - SPACE: O(1) -- technically O(n) in python since strings are immutable, had to create a List[str] then convert back to str...
#   - 2 ptr solution.

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}     # dictionary of vowels
        left, right = 0,len(s)-1                                        
        s = list(s)                 # strings are immutable in python, so convert it to list of str.
        
        while left < right:
            
            if s[left] in vowels and s[right] in vowels:    # both s[left] and s[right] have found a vowel -- swap.
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left+=1
                right-=1
            
            else:
                if not s[left] in vowels:                   # traverse left until s[left] is a vowel.
                    left+=1
                
                if not s[right] in vowels:                  # traverse right until s[right] is a vowel.
                    right-=1
                    
        return "".join(s)                                   # convert list[str] -> str