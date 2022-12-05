# problem: https://leetcode.com/problems/same-tree/
# - TIME:
# - SPACE: O(n) since you will end up creating 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:     # the trees are both empty at curr nodes 'p' and 'q'
            return True

        if (p and not q or      # one tree has hit null where another hasn't
            q and not p or
            p.val != q.val):    # the trees have mismatching node 'p' and 'q' values
            return False
                                # this statement below will compare the left and right subtrees of 'p' and 'q'. It will only return true if both return 'True'.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)