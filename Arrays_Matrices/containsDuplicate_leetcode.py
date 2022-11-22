# problem: https://leetcode.com/problems/contains-duplicate/submissions/
# - TIME: O(n), where n is length of input-list nums
# - SPACE: O(n), for the set we are creating.
#   - optimal solution. uses a set. if you have seen the number again, it would've been stored in the set.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seenNums = set()
        
        for i in range(len(nums)):
            if nums[i] in seenNums:
                return True
            seenNums.add(nums[i])
        return False