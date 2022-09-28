# problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# ASSUME THERE IS ALWAYS 1 EXACT SOLUTION FOR ANY GIVEN ARRAY

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ansList = [] # contains two indices, with two nums that add up to target
        left = 0
        right = len(numbers)-1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                ansList.extend([left+1, right+1]) # - can use two .append()'s or one .extend() for multiple elements.
                                                  # - add 1 to left, and 1 to right idx because of 1-indexed array.
                left += 1
        
        return ansList 
            