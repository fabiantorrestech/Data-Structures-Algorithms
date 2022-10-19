# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# - Utilizes Dummy node for head intialization
# - Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def recurse(self, p1: Optional[ListNode], p2: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        
        if (p1 and not p2) or (p2 and not p1) or (not p1 and not p2): # base cases for if 1 or both are empty.
            if p1 or p2:
                return p1 if p1 else p2
            else:
                return None
        
        if p1.val <= p2.val:        # always take the lesser value node as next-node, and advance the list from which we took from.
            curr.next = p1
            p1 = p1.next
        else:
            curr.next = p2
            p2 = p2.next
        curr = curr.next
        curr.next = self.recurse(p1, p2, curr)  # next node is obtained from recursion
        
        return curr
        
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, None)   # dummy head initialized to return dummy.next for 'head-intialization' in LL problems
        
        dummy.next = self.recurse(list1, list2, dummy)
        return dummy.next
        