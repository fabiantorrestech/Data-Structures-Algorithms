# problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# - TIME: O(n), where n=number of total nodes in the tree.
# - SPACE: O(n) since we must still explore every node and load it into the queue.
#
#   - Iteartive BFS with a Queue, via level-order-traversa. 
#       + A better solution that doesn't risk stack-overflow for large trees.(recursion issue)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        maxDepth = 0
        q = deque()                                 # utilizing deque as 'queue'
        q.append(root)                              # intialize the queue with root node. 
        
        while q:
            for i in range(len(q)):                 # this loop will not count all the nodes we are adding in the loop.
                                                    # this is a snapshot of the intial length of 'q' when we started the condition.
                curr = q.popleft()
                if curr.left: q.append(curr.left)   # add left and right children for next iteration of queue and to satisfy outer loop condition. (loop will only keep going if 'q' is not-empty)
                if curr.right: q.append(curr.right)
            maxDepth+=1                             # iterating through the 2nd loop will take us through the entire level of the tree. so add 1 to the depth.
        
        return maxDepth
                
            