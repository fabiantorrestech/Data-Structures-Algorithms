# problem: https://leetcode.com/problems/linked-list-cycle/
# - TIME: O(n)
# - SPACE: O(1)
#   - utilizes Floyd's Slow/Fast Ptr approach / dummyHead (no need to pay attention where if-condition is in loop).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummyHead = ListNode(0, head)
        slow, fast = dummyHead, head
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        
        return False