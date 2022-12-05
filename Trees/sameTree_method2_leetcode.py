# problem: https://leetcode.com/problems/same-tree/
# - TIME: O(m+n), where m is the size of tree 'p', and n is the size of tree 'q'.
# - SPACE: O(2m+2n) -> O(m+n).  since the list will be about the same size as the amount of nodes in 'p', and 'q'.
#                               2m and 2n since we also have to account for all the stack calls recursively.
#
#   - Utilizes recursive-DFS on each tree to make a list of all the nodes. Makes a List of str while traversing each tree.
#     Compare the lists to see if they're the same to see if they are the same tree. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recTreeToList(self, curr: Optional[TreeNode], currList: List[str]) -> None:
        
        if not curr:
            currList.append("None")
            return
        
        currList.append(str(curr.val))
        self.recTreeToList(curr.left, currList)
        self.recTreeToList(curr.right, currList)
        return
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        listP = []
        listQ = []
        
        self.recTreeToList(p, listP)
        self.recTreeToList(q, listQ)
        if listP == listQ: return True
        return False
        