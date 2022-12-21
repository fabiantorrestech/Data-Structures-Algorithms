//  *** INCOMPLETE ***


class Solution {
    
    public void printGrid(int[][] grid){
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++){
                String s1 = String.format("%d ", grid[i][j]);
                System.out.print(s1);
            }
            System.out.print(System.lineSeparator());
        }
        
    }
    
    public void recExplore(int[][] grid, int i, int j, 
                           int xOffset, int yOffset, StringBuilder currIsland){
            
        if(i<0 || i>=grid.length ||
           j<0 || j>=grid.length ||
           grid[i][j] == 0 || 
           grid[i][j]==-1){
            return;
        }
        
        grid[i][j]=-1;
        
        currIsland.append(xOffset + "" + yOffset); // add relative coordinates
        System.out.println(currIsland);
        
        recExplore(grid, i+1, j, xOffset+1, yOffset, currIsland);
        recExplore(grid, i-1, j, xOffset-1, yOffset, currIsland);
        recExplore(grid, i, j+1, xOffset, yOffset+1, currIsland);
        recExplore(grid, i, j-1, xOffset, yOffset-1, currIsland);
        
        return;
    }
    
    public int numDistinctIslands(int[][] grid) {
        
        Set<String> uniqueIslands = new HashSet<>();
        
        
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                
                if(grid[i][j]==1){
                    
                    StringBuilder currIsland = new StringBuilder();
                    recExplore(grid, i, j, 0, 0, currIsland);
                    
                    String currIslandStr = currIsland.toString();
                    if(!uniqueIslands.contains(currIslandStr)){
                        uniqueIslands.add(currIslandStr);
                    }
                }
                
            }
        }
        
        
        return uniqueIslands.size();
    }
    
}