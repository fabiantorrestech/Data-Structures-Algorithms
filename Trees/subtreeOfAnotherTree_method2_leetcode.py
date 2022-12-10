# problem: https://leetcode.com/problems/subtree-of-another-tree/
# - TIME: O(n*m), where n=size of root, m=size of subRoot
# - SPACE: O(m+n) --> 
#                   Iterative: O(n) since by using iterative-BFS, we need a queue, which will hold all 'n' nodes of root.
#                              However, since we are only creating this queue once, it stays at O(n).
#
#                   Recrusive part: O(1) in single stack call, but since we need to compare size to all 'm' nodes to
#                                   confirm if we found every single node in subTree inside root as well, this is
#                                   'm' recursive calls. so O(m) call-stack size. 
#                   
#                   So iterative O(n) + recursive = O(m)  --> ~ O(m+n)
#   - dual BFS/DFS solution. 

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkChildrenDFS(self, root, subRoot) -> bool:  # utilize recursive DFS to check if curr-root's and subRoot's left and right subtrees are equal.
        
        if not root and not subRoot: return True        # base case 1: both root and subRoot are None at same position.
        if (not root and subRoot or                     # base case 2: root and subRoot differ either in value, or one value DNE when other does. 
            root and not subRoot or
            root.val != subRoot.val): return False
        
        if root.val == subRoot.val:
            return self.checkChildrenDFS(root.left, subRoot.left) and self.checkChildrenDFS(root.right, subRoot.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        q = deque()
        q.append(root)
        while q:                        # iterate through the tree using iterative-BFS in level-order w/ queue.
            for i in range(len(q)):
                curr = q.popleft()
                
                if self.checkChildrenDFS(curr, subRoot): return True
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return False
        
        
        
        
        