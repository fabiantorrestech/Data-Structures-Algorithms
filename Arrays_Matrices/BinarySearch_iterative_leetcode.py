# 704. Binary Search
# Problem: https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #iterative implementation
        
        left = 0
        right = len(nums)-1
        
        while left <= right:    
            mid = left + int((right-left)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            
        return -1