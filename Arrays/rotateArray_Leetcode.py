"""
    Problem: https://leetcode.com/problems/remove-element/
"""

class Solution(object):
    
    def fabs_reverse_func(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start+=1
            end-=1
        return nums
    
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        
        # --- general algorithm ---
        # 1) reverse the entire array
        # 2) reverse just the first k elements
        # 3) reverse all the rest of the elements after the first k elements

        # --- BIG TIP FOR THOSE GETTING STUCK ON EDGE CASES AFTER IMPLEMENTING GENERAL ALGO ---
        #
        # required for wrap-around behavior where k > len(nums) !!
        # - in the case that k > len(nums), it will account for that and change
        # - in the normal case where k <= len(nums), it will remain unchanged.
        k=k%len(nums)

        #first reverse entire the list
        self.fabs_reverse_func(nums, 0, len(nums)-1)

        #now reverse the first k elements
        self.fabs_reverse_func(nums, 0, k-1)

        #lastly reverse the rest of the elements AFTER the first k elements.
        self.fabs_reverse_func(nums, k, len(nums)-1)

        return