# problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Method 1 - optimal solution utilizing slow and fast ptr (1 traversal)
# - TIME: O(n) -- as problem scales, we still must reassign  ptrs to 3/4 of the nodes.
# - Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:\
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next        # traverse slow at regular pace.
            fast = fast.next.next   # travese fast twice as fast as slow.
        
        return slow                 # slow will be at the middle of LL (2nd-middle node if LL is even-numbered)