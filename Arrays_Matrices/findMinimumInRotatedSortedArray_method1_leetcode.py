# problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# - TIME: O(logn)
# - SPACE: O(1)
#   - Optimal solution! (:


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        minVal = 999
        
        while left <= right:
            mid = (right-left)//2 + left
            minVal = min(nums[mid], minVal)     # keep track of min-value at every nums[mid] value 
            
            if nums[mid] > nums[right]:         # in a true sorted array, nums[mid] > nums[right] never happens, but in a rotated array, the smaller numbers lie at right end.
                left = mid+1
            else:                               # we've either overshot our estimate.
                right = mid-1
                
    
        return min(minVal, nums[0])             # covers the case where the array is "rotated n-times"/non-rotated        