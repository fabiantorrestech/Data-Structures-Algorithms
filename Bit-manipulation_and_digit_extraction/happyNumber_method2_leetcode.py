# problem: 
# - TIME: O(n)
# - SPACE: O(3n)
#   - utilizes a running hashset, a str of length 'n' (in each loop), and an array of length 'n' (in each loop)

class Solution:
    def isHappy(self, n: int) -> bool:
        
        nStr = ""
        temp = []
        seenDigits = set()
        
        while n != 1:
            nStr = str(n)                   # cast an 'n' to a string (to grab digits)
            
            for i in range(len(nStr)):      # extract n's digits -> (in a loop): turn each n's digit to int, append to temp arr.
                temp.append(int(nStr[i]))
            
            if tuple(temp) in seenDigits:   # if seen already, return false OTHERWISE add tuple(temp) into hashset
                return False
            seenDigits.add(tuple(temp))
            
            currSum = 0
            for i in range(len(temp)):      # square each digit then add it to the currSum
                currSum += temp[i]**2
            n = currSum                     # update 'n'
            temp = []                       # clear out old array.
            
        return True