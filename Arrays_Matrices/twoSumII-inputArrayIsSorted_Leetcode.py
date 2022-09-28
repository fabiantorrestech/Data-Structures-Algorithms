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
                ansList.append(left+1)  # 1-indexed array, so add 1.
                ansList.append(right+1) # 1-indexed array, so add 1.
                left += 1
        
        return ansList 