# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# - Recursion method --  reccomended
# - TIME: O(n+k), where n=number of nodes in list1, k=number of nodes in list2
# - SPACE: O(1) = no extra space needed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2 = list1, list2
        
        if (p1 and not p2) or (p2 and not p1) or (not p1 and not p2): # 3 base cases: if one or both nodes are null.
            if p1 or p2:
                return p1 if p1 else p2
            else:
                return None
        
        newNode = None
        
        if p1.val <= p2.val:    # always take the lesser value node
            newNode = p1
            p1 = p1.next
        else:
            newNode = p2
            p2 = p2.next
        
        newNode.next = self.mergeTwoLists(p1, p2) # find next node via recursion
        return newNode
        