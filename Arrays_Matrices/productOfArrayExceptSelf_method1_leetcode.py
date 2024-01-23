# problem: https://leetcode.com/problems/product-of-array-except-self/
# TIME: O(n)+O(n)=O(2n) => O(n)
# SPACE: O(1) (not counting the answer array, but if answer array is counted, then O(n))
# - Optimal solution completed with 2 passes. O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        
        # calculate the prefix products for each number in nums
        prefix = 1
        for i, num in enumerate(nums):
            ans[i] = prefix
            prefix *= nums[i]
        
        # multiply (prefix product * postfix product)
        # 1) prefix = ans[i], bc curr ans[i] is prefix product for that spot.
        # 2) ans[i] = postfix * prefix
        # 3) calculate new postfix product with nums[i].
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix = ans[i]
            ans[i] = postfix * prefix
            postfix *= nums[i]
        
        return ans