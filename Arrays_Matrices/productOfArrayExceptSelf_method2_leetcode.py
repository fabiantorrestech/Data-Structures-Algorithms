# problem: https://leetcode.com/problems/product-of-array-except-self/
# TIME: O(n) + O(n) = O(n)
# SPACE: O(1), since answer array is said to not count.
# - Non-optimal solution utilizing division.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # first multiply all numbers to get the max number
        # - we have 2 product values we multiply: product_noZeros, product_zeros
        # - product_zeros: we use this to calculate the product including zeroes.
        # - product_noZeros: we use this to calculate the product WITHOUT any zeroes.
        # - zeroesFreq: stores the number of times 0 appears in 'nums'
        product_noZeros = 1
        product_zeros = 1
        zeroesFreq = 0
        for num in nums:
            if num != 0:
                product_noZeros *= num
            product_zeros *= num
            if num == 0:
              zeroesFreq+=1
        
        # - if there is more than one 0 in nums, then answer[i] for any 'i' will be 0. so answer is all 0's.
        if zeroesFreq > 1:
            return [0]*len(nums)
        
        # now go through the array again, and answer[i] = product/nums[i]
        # - there is only one 0 OR none.
        answer = [None] * len(nums)
        
        for i,num in enumerate(nums):
            if num == 0:
                answer[i] = product_noZeros
            else:
                answer[i] = product_zeros//nums[i]
        
        
        return answer