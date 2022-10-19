# problem: https://leetcode.com/problems/max-area-of-island/
# method 2 -- utilizing set to store explored grid spots of land. does not modify original map
#           - SPACE: O(k) where k = number of 1's in grid
#           - TIME: O(m*n), where m=numRows, n=numColumns

class Solution:
    
    def printIsland(self, grid: List[List[int]]) -> None: 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end="")
            print("")
        print("")
        
    def explore(self, grid: List[List[int]], i: int, j: int, visitedLand: set[int])-> int:
        
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]==0 or (i,j) in visitedLand: # boundary checks / if its water (0) / already been visited (-1)
            return 0
        
        visitedLand.add((i,j)) 
        totalArea = 1                         # mark land as visited
        totalArea += self.explore(grid, i+1, j, visitedLand) # up
        totalArea += self.explore(grid, i-1, j, visitedLand) # down
        totalArea += self.explore(grid, i, j-1, visitedLand) # left
        totalArea += self.explore(grid, i, j+1, visitedLand) # right
        return totalArea
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visitedLand = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:                     # we've hit land
                    currArea = self.explore(grid, i, j, visitedLand) # calculate currIslandArea via DFS-recursion
                    maxArea = max(currArea, maxArea)    # is currIslandArea > maxIslandArea?
                
        return maxArea
        