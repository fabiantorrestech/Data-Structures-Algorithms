# problem: https://leetcode.com/problems/binary-tree-preorder-traversal/
# - TIME: O(n)
# - SPACE: O(n)
#   - need n space for list to store order of 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def poRec(self, root: Optional[TreeNode], ans: List[int]) -> None:
        
        if not root: return
        
        ans.append(root.val)
        if root.left or root.right:
            self.poRec(root.left, ans)
            self.poRec(root.right, ans)
        
        return
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.poRec(root, ans)
        return ans
        
        
        