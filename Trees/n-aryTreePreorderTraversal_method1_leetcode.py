# problem: https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/
# - TIME: O(n), for an n=total # nodes.
# - SPACE: O(n) - counting stack calls

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def recPreorder(self, root: 'Node', ans: List[int]) -> None:
        if root == None: return
        
        ans.append(root.val)
        for child in root.children:
            self.recPreorder(child, ans)
            
        return
    
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.recPreorder(root, ans)
        return ans
        