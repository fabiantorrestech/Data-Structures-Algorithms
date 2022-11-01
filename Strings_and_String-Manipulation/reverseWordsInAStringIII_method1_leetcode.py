# problem: https://leetcode.com/problems/reverse-words-in-a-string-iii
# TIME: O(n)
# SPACE: O(n)
# - toptimal 'pythonic' solution -- utilizing tokening str with .split(), and reverseing via slicing operators [::-1].
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()           # tokenize input str 's'
        ans = ""                # create empty str for answer ('ans')
        for word in s:
            ans += word[::-1]   # - reverse curr word
            ans += " "          # - add into 'ans'.
        
        return ans.strip()      # strip it of last trailing whitespace.