# problem: https://leetcode.com/problems/fibonacci-number/
# - TIME: O(n)
# - SPACE: O(1)
#   - optimal solution. iterative approach.

class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0: return 0         # base cases
        if n == 1: return 1
        
        fibNum1, fibNum2 = 0, 1     # FibNum1 = F(n-2),  fibNum2 =  F(n-1)
        ans = 0
        
        for i in range(2, n+1):     # calculate a fibonacci number for n>=2.
            ans = fibNum1 + fibNum2
            fibNum1 = fibNum2
            fibNum2 = ans
        
        return ans                  # ans will be the fibonacci number.