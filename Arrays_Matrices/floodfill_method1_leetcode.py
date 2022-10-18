# problem: https://leetcode.com/problems/flood-fill/
# - just a cleaner solution to my initial solution given in method 2

class Solution:
    
    def recFloodFill(self, image: List[List[int]], i, j, color, origColor) -> List[List[int]]:
        
        if i<0 or i>=len(image) or j<0 or j>=len(image[i]) or image[i][j] != origColor:     # base cases to check for out-of-bounds
                                                                                            # or if curr pixel wasn't origColor
            return image
        
        image[i][j] = color                                 # change current pixel to desired color (color)
        
        self.recFloodFill(image, i+1, j, color, origColor)  # check 1 up
        self.recFloodFill(image, i-1, j, color, origColor)  # check 1 down
        self.recFloodFill(image, i, j+1, color, origColor)  # check 1 right
        self.recFloodFill(image, i, j-1, color, origColor)  # check 1 left
            
        return image
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:  # base case: pixel is already desired color, no need to change.
            return image
        
        origColor = image[sr][sc]
        self.recFloodFill(image, sr, sc, color, origColor)
        
        return image