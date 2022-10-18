# problem: https://leetcode.com/problems/flood-fill/
# - DFS with double lists/arrays 
# - SEE METHOD 1 for cleaner SOLUTION (same algorithm)

class Solution:
    
    def printImage(self, image: List[List[int]]) -> None:
        for i in range(len(image)):
            for j in range(len(image[i])):
                print(image[i][j]," ", end="")
            print("")
        print("")
    
    def recFloodFill(self, image: List[List[int]], sr, sc, color, origColor) -> List[List[int]]:
        
        image[sr][sc] = color       # change current pixel to desired color (color)
        
        # check up, left, right, and down directions (relative to curr pixel) recursively
        i = sr
        j = sc
        
        if i+1 < len(image) and image[i+1][j] == origColor and image[i+1][j] != color:      # check 1 up
            self.recFloodFill(image, i+1, j, color, origColor)
            
        if i-1 >= 0 and image[i-1][j] == origColor and image[i-1][j] != color:              # check 1 down
            self.recFloodFill(image, i-1, j, color, origColor)

        if j+1 < len(image[i]) and image[i][j+1] == origColor and image[i][j+1] != color :  # check 1 right
            self.recFloodFill(image, i, j+1, color, origColor)
            
        if j-1 >= 0 and image[i][j-1] == origColor and image[i][j-1] != color:              # check 1 left
            self.recFloodFill(image, i, j-1, color, origColor)

        return image
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        origColor = image[sr][sc]
        self.recFloodFill(image, sr, sc, color, origColor)
        return image
