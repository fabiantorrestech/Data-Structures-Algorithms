# problem: https://leetcode.com/problems/invert-binary-tree/
# - TIME: O(n) - runs on all nodes
# - SPACE: O(n) due to all call stack size of (O(1) - only constant space needed for a temp var to store left node of tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None

        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        
        return root