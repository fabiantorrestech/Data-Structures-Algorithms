#  problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# - TIME: O(nlogn), sorted the array first, then traversed it again.
# - SPACE: O(1), no extra space declared.
#   - not the best solution, but a solution that makes sense . O(nlogn + n)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        # 1) sort the array
        # 2) find the median @ nums[len(num)/2] now that its sorted.
        # 2) see how much each element differs from mean: ans += abs(nums[i] - median) 
        
        # 1) sort the array
        nums.sort()
        
        # 2) find the median
        median = nums[len(nums)//2]
        
        # 3) find difference of each element from median
        ans = 0
        for i in range(len(nums)):
            ans += abs(nums[i]-median)
        
        return ans
    
    