# problem: https://leetcode.com/problems/number-of-distinct-islands/
# - TIME: O(n*m), where n = number of rows, m = number of columns
# - SPACE: O(k), where k is the number of distinct islands. Also number of explored land pieces, may potentially be
#          the entire grid so O(n*m). The callstack may potentially have to reach every single 
#          square on the grid, but only once O(n*m), so potentially O(n*m) for callstack memory?
#
#       - pretty optimal solution. we store frozensets of relative (x,y) coordinates into a set for each unique island.
#         In this implementation, we do not modify the original grid. explored land is stored in a set of tuples for
#         relative xOffset, yOffset (x,y).

class Solution:
    
    def explore(self, grid, i, j, xOffset, yOffset, currIsland, exploredLand) -> None:
        
        if (i<0 or i>=len(grid) or                  # base cases: out of bounds on i or j, exploring already-explored land, or hit water
            j<0 or j>=len(grid[0]) or
            grid[i][j]==0 or (i,j) in exploredLand):
            return
        
        exploredLand.add((i,j))             # mark this piece of land as explored (global set)
        currIsland.add((xOffset, yOffset))  # mark down relative coordinates for this piece of land
        
        self.explore(grid, i+1, j, xOffset+1, yOffset, currIsland, exploredLand)    # recursive-DFS on 4 cardinal directions.
        self.explore(grid, i-1, j, xOffset-1, yOffset, currIsland, exploredLand)
        self.explore(grid, i, j+1, xOffset, yOffset+1, currIsland, exploredLand)
        self.explore(grid, i, j-1, xOffset, yOffset-1, currIsland, exploredLand)
        
        return
    
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        exploredLand, uniqueIslands = set(), set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                currIsland = set()
                if grid[i][j]==1:
                    initX, initY = 0, 0
                    self.explore(grid, i, j, initX, initY, currIsland, exploredLand)
                
                if currIsland:
                    uniqueIslands.add(frozenset(currIsland))
        
        return len(uniqueIslands)