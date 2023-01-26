# problem: https://leetcode.com/problems/container-with-most-water
# - TIME: O(n)
# - SPACE: O(1)
#   - optimal linear time solution. (: Two pointer problem.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeight = 0
        
        h1, h2 = 0, len(height)-1
        while h1 < h2:
            area = (h2-h1) * min(height[h2], height[h1])
            maxHeight = max(area, maxHeight)

            # find smaller side and raise it up
            smaller = min(height[h1], height[h2])
            if smaller == height[h1]:
                h1 += 1
            else:
                h2 -= 1
            
        return maxHeight
        