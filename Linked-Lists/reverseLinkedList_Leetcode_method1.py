# problem: https://leetcode.com/problems/reverse-linked-list/
# - iterative solution -- most optimal O(n) runtime, O(1) memory.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr, prev = head, None
        
        while curr:
            ptr2 = curr.next
            curr.next = prev
            prev = curr
            curr = ptr2
            
        return prev