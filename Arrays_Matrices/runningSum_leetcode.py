# problem: https://leetcode.com/problems/running-sum-of-1d-array/
# - TIME: O(n)
# - SPACE: O(n) -- for answer list
#   - optimal solution.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            ans.append(temp)
        return ans