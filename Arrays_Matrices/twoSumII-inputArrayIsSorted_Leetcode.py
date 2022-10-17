# problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# ASSUME THERE IS ALWAYS 1 EXACT SOLUTION FOR ANY GIVEN ARRAY

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1
        
        while left < right:
            sumLR = numbers[left] + numbers[right]
            
            if sumLR == target:
                return [left+1, right+1]
            elif sumLR < target:
                left+=1
            else:
                right-=1
            