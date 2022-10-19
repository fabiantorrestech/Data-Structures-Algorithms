# problem: https://leetcode.com/problems/max-area-of-island/
# method1 -  no extra memory needed (O(m*n)), m=numRows, n=numColumns


class Solution:
    
    def printIsland(self, grid: List[List[int]]) -> None: 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end="")
            print("")
        print("")
        
    def explore(self, grid: List[List[int]], i: int, j: int) -> int:
        
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]==0 or grid[i][j]==-1: # boundary checks / if its water (0) / already been visited (-1)
            return 0
        
        grid[i][j] = -1                       # - mark the current land spot as 'explored' 
        totalArea = 1
        totalArea += self.explore(grid, i+1, j) # up
        totalArea += self.explore(grid, i-1, j) # down
        totalArea += self.explore(grid, i, j-1) # left
        totalArea += self.explore(grid, i, j+1) # right
        return totalArea
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:                     # we've hit land
                    currArea = self.explore(grid, i, j) # calculate currIslandArea via DFS-recursion
                    maxArea = max(currArea, maxArea)    # is currIslandArea > maxIslandArea?
                
        return maxArea
        