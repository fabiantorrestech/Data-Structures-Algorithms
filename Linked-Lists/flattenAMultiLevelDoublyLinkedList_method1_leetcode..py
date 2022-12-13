# problem: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# - TIME: O(n)
# - SPACE: O(k), where k is the number of child nodes.
#   - UTILIZE STACK! very fast and easy to understand solution, to append old curr.next's until the end! (:


from collections import deque
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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        stack = deque()
        curr = head
        
        while curr:
            
            if curr.child:                              # make curr.next == curr.child AND remove connection to curr.child via child ptr.
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child # link forwards: curr -> child
                curr.next.prev = curr  # link backwards: curr <-> child
                curr.child = None      # removes curr.child ptr -- now curr.next -> curr.child
            
            
            if curr.next == None and stack:             # Reached end of doubly LL -- append the old curr.nexts that we stored in the stack.
                curr.next = stack.pop() # forward link
                curr.next.prev = curr   # backwards link
                
            curr = curr.next
        
        return head