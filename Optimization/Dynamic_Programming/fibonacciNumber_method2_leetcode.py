# problem: https://leetcode.com/problems/fibonacci-number/
# - TIME: O(n)
# - SPACE: O(n)- must make ~n stack frames to solve.
#   - recursive solution (NON-optimal for space complexity)

class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0: return 0
        if n == 1: return 1
        
        return self.fib(n-2) + self.fib(n-1)