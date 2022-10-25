# problem: https://leetcode.com/problems/find-pivot-index/
# TIME: O(n)
# SPACE: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum, leftSum, rightSum = 0, 0, 0
        
        for i in range(len(nums)):  # get the totalSum
            totalSum+=nums[i]
        rightSum = totalSum
        
        for i in range(len(nums)):  # use totalSum to calculate LS and RS while traversing
            rightSum-=nums[i]
            
            if leftSum == rightSum: # found pivotIdx!
                return i
            
            leftSum += nums[i]      # ls != rs, so calculate leftSum for next calculation
        
        return -1                   # no pivotIdx exists.
        