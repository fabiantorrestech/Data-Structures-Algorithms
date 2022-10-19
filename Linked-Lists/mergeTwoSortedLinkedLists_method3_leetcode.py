# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# - utilizes dummy Node
# - NO RECURSION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,None)        # a way with dealing with no head of LL
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if (list1 and not list2) or (list2 and not list1):
            curr.next = list1 if list1 else list2
        
        return dummy.next