# problem: https://leetcode.com/problems/rotate-array

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
        
        