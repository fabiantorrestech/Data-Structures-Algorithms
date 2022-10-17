#problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    
    # given a List[str], reverses the List[str] AND returns it as a str.
    def reverseWord(self, string: List[str], l: int, r: int) -> str:
        while l < r:
            temp = string[l]
            string[l] = string[r]
            string[r] = temp
            l+=1
            r-=1
        return ''.join(string)
    
    def reverseWords(self, s: str) -> str:
        
        listOfStr = s.split()   # tokenize string in python by splitting at space (default for .split() method)
        result = ""
        for i in range(len(listOfStr)):
            elem = listOfStr[i]                                     # treat each token of str as its own string
            result+=self.reverseWord(list(elem), 0, len(elem)-1)    # reverse elem and append it result.
            result+=" "                                             # append a space to result
        
        return result.strip()                                       # strip off trailing white space