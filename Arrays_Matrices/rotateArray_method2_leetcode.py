# problem: https://leetcode.com/problems/rotate-array/?envType=study-plan&id=algorithm-i 
# visualization with logs: https://imgur.com/a/tyG1nim, https://imgur.com/a/ixou5SQ

class Solution:
    
    # performs in-place reversal of a list from start to finish
    # left = first index to start reversing from. (inclusive)
    # right = last index to reverse until (inclusive)
    def reverseGivenList(self, myList: List[int], left: int, right: int) -> None:
        while left < right:
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
            left += 1
            right -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        if k < 0:
            k += len(nums)
        
        nums.reverse()                          # reverse the entire list ('n' elements)
        self.reverseGivenList(nums, 0, k-1)     # reverse the first 'k' elements
        self.reverseGivenList(nums, k, len(nums)-1) # reverse the remaining n-k elements. 