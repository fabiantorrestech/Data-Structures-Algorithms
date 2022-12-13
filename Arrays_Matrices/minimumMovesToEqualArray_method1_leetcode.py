# problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# - TIME: O(n)
# - SPACE: O(1)
#   - 1 pass, if min is not allowed, then 2 passes to get the minimum element.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        # n-1 elements increasing by 1 <==> 1 element decreasing by 1
        # we can just take the difference between all elements and minElement and add up all differences.
        #
        # nums[i] - x = minElement --> nums[i] - minElement = x
        #
        # then simply add up all the x's! that is the answer!

        ans = 0
        minElement = min(nums)
        for i in range(len(nums)):
            ans+= nums[i] - minElement # n
        return ans
        