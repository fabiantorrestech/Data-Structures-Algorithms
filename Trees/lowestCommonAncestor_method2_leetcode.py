# problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# - TIME: O(n)
# - SPACE: O(2n) -> O(n)
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def printDict(self, currDict) -> None:
        for key in currDict:
            print(f"currDict[{key}]: {currDict[key].val}")
        print("")
    
    def findNode(self, curr, target , currDict) -> None:
        i = 0
        while curr != target:
            if target.val > curr.val:
                currDict[i] = curr
                curr = curr.right
            elif target.val < curr.val:
                currDict[i] = curr
                curr = curr.left
            i+=1
        currDict[i] = curr

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None: return None
        
        pDict , qDict = dict(), dict()
        self.findNode(root, p, pDict)
        self.findNode(root, q, qDict)
        
        
        LCA = None
        maxDictSize = max(len(pDict), len(qDict))
        for i in range(maxDictSize):
            if ((pDict.get(i) and qDict.get(i)) and
                (pDict[i] == qDict[i])):
                LCA = pDict[i]
            else:
                break
        return LCA
        