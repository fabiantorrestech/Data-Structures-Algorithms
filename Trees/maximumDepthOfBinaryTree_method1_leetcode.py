# problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# - TIME: O(n)
# - SPACE: O(n), since we use O(1) memory for each call, but we call the function n-times recursively. 
#   - an acceptable solution utilizing recursive DFS approach.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        maxDepth=1
        maxDepth+=max(self.maxDepth(root.left), self.maxDepth(root.right))

        return maxDepth

