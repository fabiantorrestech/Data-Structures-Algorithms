# problem: https://leetcode.com/problems/rotate-array/?envType=study-plan&id=algorithm-i 
# - TIME: O(n)
# - SPACE: O(1), no extra memory needed
#   - optimal solution!
# visualization with logs: https://imgur.com/a/tyG1nim, https://imgur.com/a/ixou5SQ

class Solution:
    
    # modifies list in place.
    def reverseList(self, l: list[int], left: int, right: int) -> None:
        while left < right:
            temp = l[left]
            l[left] = l[right]
            l[right] = temp
            left+=1
            right-=1
        return
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for 'k' values > nums's size. (ex: len(nums)=7, k=9 --> k=k%len(nums) --> k=9%7 --> k=2)
        if k > len(nums):
            k = k%len(nums)
            
        # reverse the entire list once
        self.reverseList(nums, 0, len(nums)-1)
        # reverse the first '0 to k-1' elements of the list
        self.reverseList(nums, 0, k-1) 
        # reverse the last 'k to n' elements of the list
        self.reverseList(nums, k, len(nums)-1)
        
        return
        