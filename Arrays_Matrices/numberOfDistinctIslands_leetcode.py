
# NEED EXPLANATION!!!


class Solution:
    
    def explore(self, grid, i, j, currIsland, xOffset, yOffset) -> None:
        
        if (i<0 or i>=len(grid) or
            j<0 or j>=len(grid[0]) or
            grid[i][j]==-1 or grid[i][j]==0):
            return
        
        grid[i][j] = -1                                                 # mark current spot as explored
        currIsland.add((xOffset,yOffset))                               # add tuple(x,y) to currIsland set
        self.explore(grid, i+1, j, currIsland, xOffset+1, yOffset)
        self.explore(grid, i-1, j, currIsland, xOffset-1, yOffset) 
        self.explore(grid, i, j+1, currIsland, xOffset, yOffset+1) 
        self.explore(grid, i, j-1, currIsland, xOffset, yOffset-1) 
        
        return
        
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        uniqueIslands = set()
        seenCoors = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                currIsland = set()          #set of local coordinates of
                if grid[i][j]==1:
                    print(f"found a piece of land at i:{i}, j:{j}")
                    self.explore(grid, i, j, currIsland, 0, 0)
                    print(f"currIsland: {currIsland}")
                
                if currIsland:
                    uniqueIslands.add(frozenset(currIsland))
                
                # now compare the exploredLand[(x,y)] to our seenCoors.
                
        
        return len(uniqueIslands)