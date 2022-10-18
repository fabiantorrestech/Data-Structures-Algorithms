# problem: https://leetcode.com/problems/merge-two-binary-trees/

# Time: O(n) = combined number of nodes between root1 and root2
# Space: O(n) = combined amount of time n where n is the time is takes to traverse root1's + root2's entire trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 and not root2:                               # base case 1
            return root1
        elif root2 and not root1:                             # base case 2
            return root2
        elif not root1 and not root2:                         # base case 3
            return None
        
        newNode = TreeNode(root1.val + root2.val)              # create a new treeNode with sum
        newNode.left = self.mergeTrees(root1.left, root2.left)    # add up vals of left-nodes
        newNode.right = self.mergeTrees(root1.right, root2.right) # add up vals of right-nodes
        
        return newNode