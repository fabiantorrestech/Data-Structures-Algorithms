# problem: https://leetcode.com/problems/max-area-of-island/
# ---- NOT FINISHED YET --- 

class Solution:
    
    def printIsland(self, grid: List[List[int]]) -> None: 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end="")
            print("")
        print("")
        
    def explore(self, grid: List[List[int]], i: int, j: int) -> int:
        
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]==0: # boundary checks / if its water (0)
            return 0
        
        print("i: ", i, "j: ", j, "\n")
        totalArea=1
        grid[i][j] = -1                       # - mark the current land spot as 'explored' 
        totalArea+=self.explore(grid, i+1, j) # up
        totalArea+=self.explore(grid, i-1, j) # down
        totalArea+=self.explore(grid, i, j-1) # left
        totalArea+=self.explore(grid, i, j+1) # right
        
        return totalArea
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    currArea = self.explore(grid, i, j)
            
            maxArea = max(currArea, maxArea)
                
        
        return maxArea