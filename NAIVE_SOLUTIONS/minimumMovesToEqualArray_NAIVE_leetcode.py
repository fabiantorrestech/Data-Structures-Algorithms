class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        ans = 0
        while True:
            minElement = min(nums)
            maxElement = max(nums)
            maxIdx = nums.index(maxElement)
            
            if minElement == maxElement: return ans # once max == min, we are done.
            
            for i in range(len(nums)):
                if i == maxIdx: # do not add 1 to the max in 'nums'.
                    continue
                
                nums[i]+=1      # add 1 to all other elements.
            ans+=1          # adding 1 to all other elements in 1 loop iteration counts as 1 step.