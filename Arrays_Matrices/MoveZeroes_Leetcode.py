# problem: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums)-1
        
        while left < right:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right-=1
            else:
                left+=1
        
        return nums