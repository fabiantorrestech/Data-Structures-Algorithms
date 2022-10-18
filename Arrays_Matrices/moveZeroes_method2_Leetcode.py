# problem: https://leetcode.com/problems/move-zeroes/
# - NOT PREFERRED SOLUTION 
# - using python pop and append list methods!

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0,0
        
        while right < len(nums):
            
            if nums[left] == 0 and nums[right] != 0:    # swap L and R!
                nums[left] = nums[right]
                nums[right] = 0
                left+=1
            
            elif nums[left] != 0:                       # keep incrementing L until its at a 0
                left+=1
                
            right+=1                                    # keep incrementing R to find a non-zero element.
        
        return nums