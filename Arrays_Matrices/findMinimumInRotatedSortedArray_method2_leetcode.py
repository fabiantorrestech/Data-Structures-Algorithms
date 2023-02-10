# problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# - TIME: O(n)
# - SPACE: O(1)
#   - slightly less optimal solution that runs in O(n) time if the array has been rotated n-1 times, then the extra step
#     will take n-1 times to find the correct left boundary.



class Solution:
    
    # we assume all nums b/t nums[left] -- nums[right] are sorted.
    # - so normal Binary Search rules apply. We want the minimum value, so target is whichever way has smaller numbers (typically left)
    def bs(self, nums, left, right):
        
        minVal = 999
        
        while left <= right:
            mid = (right-left)//2 + left
            
            minVal = min(nums[mid], minVal)
            if nums[mid] > nums[mid-1]:         # always look back 1 value (prevents out of range) to gauge if we want to focus on right window ...
                right = mid-1
            elif nums[mid] < nums[mid-1]:       # ... or left window
                left = mid+1
    
        return minVal
    
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return nums[0]        # base case for input array of size 1
        
        left, right = 0, len(nums)-1
        if nums[left] > nums[right]:            # run an extra step for rotated arrays. move left pivot until we get ONLY the sorted part. 
                                                # - note: if the array has been rotated, nums[left] > nums[right] is always true for at least 1 iteration.
            while nums[left] > nums[right]: 
                left+=1
            
        return self.bs(nums, left, right)       # run normal Binary Search with adjusted L, R boundaries.
                
        