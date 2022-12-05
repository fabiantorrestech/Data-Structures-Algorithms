# problem: https://leetcode.com/problems/invert-binary-tree/
# - TIME: O(n) - runs on all nodes
# - SPACE: O(n) due to all call stack size of (O(1) - only constant space needed for a temp var to store left node of tree)
#       - the idea is to simply reverse 1 subtree at a time (reverse all small subtrees in left, then in right), then by the
#         time we return to root, simply swap left and right again. we have now inverted the entire tree from left to right.
#       - Do an example on paper to fully understand... focus on one node,  then a 3 node binary-tree, then 7 node one. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None # base case: if we hit a "NULL" node (nonexistant children)
        
        temp = self.invertTree(root.left)       # temp = left
        root.left = self.invertTree(root.right) # new-left = right
        root.right = temp                       # right = temp (left)
        
        return root
        
        
            
            
        
        