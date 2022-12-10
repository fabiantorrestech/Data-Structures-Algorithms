# problem: https://leetcode.com/problems/subtree-of-another-tree/
# - TIME: O(m*n), where n = size of root, m = size of subRoot
# - SPACE: O(m) --> O(1) in each call-stack call, but since there's 'm' nodes in subRoot to compare to, its O(m).
#   - optimal solution utilizing 'sameTree' solution from leetcode. Recursive DFS.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:                        # the trees are both empty at curr nodes for 'root' and 'subRoot'
            return True
                                
        if root and subRoot and root.val == subRoot.val:    # we found a node.val match -- compare the left and right subtrees
                                                            # of 'root' and 'subRoot'. It will only return true if both return 'True'.
            return (self.isSameTree(root.left, subRoot.left) and
                    self.isSameTree(root.right, subRoot.right))
        
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot: return True                            # base case 1: both nodes do not exist.
        if not root and subRoot or root and not subRoot: return False       # base case 2: if 1 node doesn't exist.
        
        if self.isSameTree(root,subRoot): return True                       # recursively compare curr 'root' subTree vs curr 'subRoot' tree.
            
        return (self.isSubtree(root.left, subRoot) or                       # look in left and right children in 'root' to find a same subTree.
                self.isSubtree(root.right, subRoot))
        
        return False