# problem: https://leetcode.com/problems/missing-number/
# - TIME: O(n)
# - SPACE: O(n)
#   - Pretty fast, but not the most efficient solution.  Most intuitive solution. Utilize a hashmap to store all of nums then loop through 0 to n to find which number is missing from nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # store all numbers in to a hashmap: <k,v> -> <i, nums[i]>
        seenNums = dict()
        for i in range(len(nums)):
            seenNums[nums[i]] = i
        
        # now loop through with a counter to see which is missing from 0 to n
        for i in range(0, len(nums)+1):
            if i not in seenNums:
                return i
        
        return 0