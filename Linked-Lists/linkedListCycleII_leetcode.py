# problem: https://leetcode.com/problems/linked-list-cycle-ii/
# - TIME: O(n)
# - SPACE: O(n) - for hash-set/set to store seenNodes.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        seenNodes = set()           # set to store seen LL nodes
        
        while curr:
            if curr in seenNodes:   # compare curr node to all seenNodes. if it is in set, it has already been seen. return curr.
                return curr
            
            seenNodes.add(curr)     # new node discovered --  add it to seenNodes.
            curr = curr.next
            
        return None                 # if it reaches here, it had no cycle.
            