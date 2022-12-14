# problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# - TIME: O(n)
# - SPACE: O(n) --  O(1) for each stack-call, but stack at worst will grow to be the size of number of children in list.
#                   If every node has a child, then it can grow to be as large as O(n) worst case.
# 
#   - less optimal and a bit more challenging approach to use recursive-DFS. 


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def dfsExplore(self, curr) -> 'Optional[Node]':
        
        while curr:
            if curr.child:
                oldNext = curr.next                 # store oldNext: curr -> curr.next (oldNext) 
                tail = self.dfsExplore(curr.child)  # traverse through child, last Node = tail
                curr.next = curr.child              # fwd route curr.next: curr -> curr.child
                curr.next.prev = curr               # bckwds route curr.next.prev: curr <-> curr.child
                tail.next = oldNext                 # fwd route child's tail to oldNext: tail -> oldNext
                if oldNext:                         # if oldNext wasn't None, bckwds route it to tail: tail <-> oldNext
                    oldNext.prev = tail
                curr.child = None                   # break reference to child via curr.child
            
            prev = curr
            curr = curr.next
        
        return prev
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        while curr:
            if curr.child:              # hand it off to a helperDFS function to recursively handle children
                self.dfsExplore(curr)
            
            curr = curr.next
        
        return head
        