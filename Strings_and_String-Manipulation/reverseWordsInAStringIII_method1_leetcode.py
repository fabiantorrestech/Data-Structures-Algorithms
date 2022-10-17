# problem: https://leetcode.com/problems/reverse-words-in-a-string-iii
# - this is a shorter solution if they allow you to use slice operator to reverse tokenized strings.

class Solution:
    
    def reverseWords(self, s: str) -> str:
        
        listOfStr = s.split()   # tokenize string in python by splitting at space (default for .split() method)
        result = ""
        
        for i in range(len(listOfStr)):
            elem = listOfStr[i]     # treat each token of str as its own string
            result+=elem[::-1]      # use slice operator to reverse elem, add it to result 
            result+=" "             # append a space to result
        
        return result.strip()       # strip off trailing white space