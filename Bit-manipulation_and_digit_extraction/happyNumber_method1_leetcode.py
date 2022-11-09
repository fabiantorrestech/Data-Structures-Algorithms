# problem: 
# - TIME: O(n)
# - SPACE: O(n)
#   - utilizes a running hashset, but otherwise, very efficient.

class Solution:
    
    def extractDigits(self, n: int) -> int:
        
        tempSum = 0
        while n != 0:
            digit = n%10            # gives us the ones position digit
            tempSum += digit**2     # add squaredDigit to tempSum
            n = n//10               # update n and 'remove' the digit from view
            
        return tempSum
    
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1:
            
            if n in seen:               # found a cycle. return False
                return False
            
            elif n not in seen:         # store n in 'seen' hashset
                seen.add(n)
                
            n = self.extractDigits(n)   # extract digits, square each one, sum them all, return the sum of sqrd digits.
        
        return True                     # n must be 1 at this point. it is a happy number. (:
            
        