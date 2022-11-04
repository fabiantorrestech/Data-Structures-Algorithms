# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def recValidBST(self, curr: Optional[TreeNode], leftBoundary: int, rightBoundary: int) -> bool:
        
        if not curr: return True                                        # base case / empty tree is a valid BST.
        
        if curr.val <= leftBoundary or curr.val >= rightBoundary:       # leftBoundary < curr < rightBoundary
            return False
        
        left, right = curr.left, curr.right
        leftResult = self.recValidBST(left, leftBoundary, curr.val)     # traverse left child, update rightBoundary.
        rightResult = self.recValidBST(right, curr.val, rightBoundary)  # traverse right child, update leftBoundary.
        
        if leftResult and rightResult:                                  # left and right must be valid to be a valid BST
            return True
    
        return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recValidBST(root, float("-inf"), float("inf"))      # solve via recursion
                                                                        # - initial upperBound = +infinity, lowerBound = -infinity