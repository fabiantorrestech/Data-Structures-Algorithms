# problem: https://leetcode.com/problems/combinations/
# - TIME: O(k * n^k) in code, but in theory, O(k * nCk)
# - SPACE: O(nCk)
# brute force solution, which happens to be the only solution.  

class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start: int, comb: List[int]) -> None:
            if len(comb) == k:
                ans.append(comb.copy()) # we will continue to modify comb to make new combinations. so append a snapshot of it as it is.
                return
            
            for i in range(start, n+1):
                comb.append(i)          # start = i,
                                        # ex: for n=4, k=2, it will append:
                                        # - [1,2]->RETURN->[1]->[1,3]->return->[1,4]->
                                        # 
                backtrack(i+1, comb)    # recursively call for next child in decision tree.
                comb.pop()              # pop the last value from the python list.
            
        backtrack(1, [])
        return ans
        
        