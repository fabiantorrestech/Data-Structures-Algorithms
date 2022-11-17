#problem: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# - TIME: O(n), where n=number of nodes in Binary Tree
# - SPACE: O(n), since we need to store each node's value once, then store all levels into one array.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        ans = []
        q = deque()                 # use a deque as a 'queue' (.append() at right, .popleft() at left)
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)): # empty out q of nodes of currLevel (into level[]).
                curr = q.popleft()
                level.append(curr.val)
                
                if curr.left: q.append(curr.left)   # Then add all L-R children of currLevel nodes at this level to q for next level[] iteration.
                if curr.right: q.append(curr.right)
            ans.append(level)       # add currLevel to answer.
        
        return ans