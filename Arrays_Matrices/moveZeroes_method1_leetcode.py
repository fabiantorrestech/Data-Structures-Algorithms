# problem: https://leetcode.com/problems/move-zeroes/
# - PREFERRED SOLUTION WIH 2 PTRS that probably solves it as intended

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0,0
        
        while right < len(nums):
            
            if nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left+=1
            
            elif nums[left] != 0:
                left+=1
                
            right+=1
        
        return nums