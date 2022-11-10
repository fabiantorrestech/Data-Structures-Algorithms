# problem: https://leetcode.com/problems/linked-list-cycle-ii/
# - TIME: O(n) - only need to traverse the linked list some limited number of times for all the nodes in the LL
# - SPACE: O(1)
#   - utilizes floyd's slow-fast ptr approach.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:            # detected that a cycle exists
                slow = head             
                while slow != fast:     # now need to find where exactly cycle loops around to
                                        # set slow=head, then traverse slow and fast by 1 both until equal.
                    slow = slow.next
                    fast = fast.next
                return slow
            
        return None