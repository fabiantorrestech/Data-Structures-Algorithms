# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# still optimal solution, but not very clean... No dummy head utilized. (check method 3 & 4 for more elegant clean solution.)
# - NO RECURSION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 and not list2) or (list2 and not list1):  # base case: given 1 empty list
            return list1 if list1 else list2
        
        p1, p2 = list1, list2
        newHead, newCurr = None, None   # need a newHead to return at end.
        
        while p1 and p2:
            if newHead == None:         # assigning newHead (to return at end)
                if p1.val <= p2.val:
                    newHead = p1
                    p1 = p1.next
                else:
                    newHead = p2
                    p2 = p2.next
                newCurr = newHead
                
            else:                       # logic for rerouting rest of ptrs of list using newCurr.
                if p1.val <= p2.val:
                    newCurr.next = p1
                    p1 = p1.next
                else:
                    newCurr.next = p2
                    p2 = p2.next
                    
                newCurr = newCurr.next
        
        if p1 or p2:                    # covers any remaining nodes
            newCurr.next = p1 if p1 else p2 
            
        return newHead