# problem: https://leetcode.com/problems/two-sum/
# - TIME: O(n)
# - SPACE: O(n) 
# - Also Optimal Solution using hashtable -- more concise syntax using enumerate()

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # a + b = c
        # a = currNum
        # b = numToLookForInDict
        # c = target
        #
        # b = c - a
        
        seenNums = dict()
        for i, n in enumerate(nums):                # i = idx, n = nums[idx]
            numToFind = target - n
            
            if seenNums.get(numToFind) != None:     # if seenNums[numToFind] != None, return the list []
                return [seenNums[numToFind], i]
            
            seenNums[n] = i                         # store seenNums[currNum] if we couldn't find the other number yet.