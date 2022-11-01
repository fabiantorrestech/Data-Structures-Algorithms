# problem: https://leetcode.com/problems/linked-list-cycle/
# - TIME: O(n)
# - SPACE: O(1)
#   - utilizes Floyd's Slow/Fast Ptr approach / no dummyHead (PREFERRED)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        
        