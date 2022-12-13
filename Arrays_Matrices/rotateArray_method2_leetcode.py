# problem: https://leetcode.com/problems/rotate-array
# - TIME: O(k), will make k swaps.
# - SPACE: O(1), no extra space allocated
#   - 'pythonic' way to solve this problem. not optimal though...
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        right = len(nums)-1
        
        for i in range(k):
            temp = nums[right]
            nums.pop()
            nums.insert(0, temp)
        
        