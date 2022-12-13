# problem: https://leetcode.com/problems/number-of-distinct-islands/
# - TIME: O(n*m), where n = number of rows, m = number of columns
# - SPACE: O(k), where k is the number of distinct islands. The callstack may potentially have to reach every single 
#          square on the grid, but only once O(n*m), so potentially O(n*m) for callstack memory?
#
#       - pretty optimal solution. we store frozensets of relative (x,y) coordinates into a set for each unique island.
#         In this implementation, we are allowed to modify the grid to marked explored land pieces (1->-1).


class Solution:
    
    def explore(self, grid, i, j, currIsland, xOffset, yOffset) -> None:
        if (i<0 or i>=len(grid) or              # base cases: if i in-bounds...
            j<0 or j>=len(grid[0]) or           #             if j in-bounds...
            grid[i][j]==-1 or grid[i][j]==0):   #             if we hit an already-explored land-piece (-1) or water (0)
            return
        
        grid[i][j] = -1                                                 # mark current spot as explored
        currIsland.add((xOffset,yOffset))                               # add tuple(x,y) to currIsland set
        self.explore(grid, i+1, j, currIsland, xOffset+1, yOffset)
        self.explore(grid, i-1, j, currIsland, xOffset-1, yOffset) 
        self.explore(grid, i, j+1, currIsland, xOffset, yOffset+1) 
        self.explore(grid, i, j-1, currIsland, xOffset, yOffset-1) 
        
        return
        
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        uniqueIslands = set()               # set of all relative x-y coordinates of all diff islands! 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                currIsland = set()          # set of local coordinates for currentIsland found at grid[i][j]
                if grid[i][j]==1:
                    self.explore(grid, i, j, currIsland, 0, 0)
                
                # if our currIsland set of relative-coordinates is not empty, we add it as a frozenset to our set.
                # - ***IMPORTANT*** we can add frozensets since they're immutable.
                # -                  PLUS, since they're being added to sets, duplicates wont be counted!
                if currIsland:
                    uniqueIslands.add(frozenset(currIsland))
                
                
                
        
        return len(uniqueIslands)