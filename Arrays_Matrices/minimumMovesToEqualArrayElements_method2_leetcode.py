# problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# - TIME: O(nlogn)
# - SPACE: O(1)
#   - Same approach as method1, but slightly less optimal. Takes O(nlogn) time to sort the function. Then takes O(n) time to run through loop iteration again to find how many steps for each element. O(nlogn + n) -> O(nlogn) 


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums.sort()
        steps = 0
        for i in range(len(nums)-1, -1, -1): # loop backwards from max to min: min <- max
            if nums[i]==nums[0]: break  # if any element before the min == min's value, we are finished. 
            steps+=nums[i]-nums[0]      # see how many steps until we reach the min for curr-value.
        
        return steps
        