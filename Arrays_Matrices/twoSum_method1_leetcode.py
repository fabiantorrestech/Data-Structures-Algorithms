# problem: https://leetcode.com/problems/two-sum/
# - TIME: O(n)
# - SPACE: O(n) 
# - Optimal Solution using hashtable

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # a + b = c, where a=currNum and c=target, but we can rewrite it like so...
        # b = c - a
        
        seenNumbers = {}
        
        for i in range(len(nums)):                      # loop through array. do nums[i] - target = -numToFindInDictionary
            numToFind = target - nums[i]
            
            if (numToFind in seenNumbers and i != seenNumbers[numToFind]):
                    return [i, seenNumbers[numToFind]]
                
            seenNumbers[nums[i]] = i                    # if there is no solution found, store the current number in our hashmap.
        