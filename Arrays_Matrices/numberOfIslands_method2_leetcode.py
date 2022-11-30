# problem: https://leetcode.com/problems/number-of-islands/
# - TIME: O(r*c), where r = numRows, c = numCols. 
# - SPACE: O(1)
#   - Recursive DFS Solution (if you are allowed to change the grid's values)

class Solution:
    
    def printGrid(self, grid: List[List[str]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(f"{grid[i][j]} ", end = "")
            print(" ")
        print(" ")
    
    def recFindIsland(self, grid: List[List[str]], i:int, j:int) -> int:
        if (i<0 or i>=len(grid) or
            j<0 or j>=len(grid[i]) or
            grid[i][j] == "0" or
            grid[i][j] == "-1"):        # base case for recursion: if we go out of bounds, or hit already-explored land, or we hit water (0)
            return 0
        
        grid[i][j] = "-1"                # mark this plot of land as explored (-1) 
                                         # - now, check its adjacent land masses to explore them.
        self.recFindIsland(grid, i+1, j) # travel 1 down
        self.recFindIsland(grid, i-1, j) # travel 1 up
        self.recFindIsland(grid, i, j+1) # travel 1 right
        self.recFindIsland(grid, i, j-1) # travel 1 left
        return True
        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 0 = water
        # 1 = land
        # -1 = explored land
        
        totalNumIslands = 0
        isIsland = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":    # once we find land, explore the whole island recursively and mark the whole island as explored.
                    isIsland = self.recFindIsland(grid, i, j)
                if isIsland == True:     # add the explored island to our total.
                    totalNumIslands+=1
                isIsland = False
                
        return totalNumIslands