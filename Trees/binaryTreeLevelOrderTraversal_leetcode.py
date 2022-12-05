#problem: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# - TIME: O(n), where n=number of nodes in Binary Tree
# - SPACE: O(n), since we need to store each node's value once, then store all levels into one array.

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        result = []             # answer list
        q = deque()             # used as a queue
        q.append(root)          # need to intialize queue with root node.
        
        while q:                                        # loop through while the q isn't empty.
            temp = []                                   # create temp[] list to store all nodes in this level
            
            for i in range(len(q)):                     # - range(len(q)) takes a snapshot of how long the queue is for this level
                                                        #   (not counting the nodes we will add for the next level while in the loop). 
                curr = q.popleft()
                if curr.left: q.append(curr.left)       # these 2 statements are where we add in the children of curr nodes for next iteration
                if curr.right: q.append(curr.right)
                temp.append(curr.val)
            result.append(temp)                         # append current level temp[] list to the answer of lists.
        
        return result