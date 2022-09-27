class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = []
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            numsLeftSqrd = nums[left] ** 2 
            numsRightSqrd = nums[right] ** 2 
            
            if numsLeftSqrd > numsRightSqrd:
                answer.append(numsLeftSqrd)
                left += 1
            elif numsLeftSqrd < numsRightSqrd:
                answer.append(numsRightSqrd)
                right -= 1
            else:
                answer.append(numsLeftSqrd)
                left += 1
                
        return answer[::-1]