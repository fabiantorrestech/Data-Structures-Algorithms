#  problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# - TIME: O(nlogn), sorted the array first, then traversed it again.
# - SPACE: O(1), no extra space declared.
#   - still not the most optimal solution, but more intuitive. 2 pointer approach O(nlogn + logn)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        # 1) sort the array
        # 2) use two pointers and find what we need to make nums[left] == nums[right]. start from left and right and go while left < right.
        
        # 1) sort the array
        nums.sort()
        
        # 2) 2 pointer approach
        ans = 0
        left, right = 0, len(nums)-1
        while left < right:
            ans += abs(nums[right]-nums[left])
            left+=1
            right-=1
            
        return ans
    
    