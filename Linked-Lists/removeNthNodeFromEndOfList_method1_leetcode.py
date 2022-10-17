# problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# optimal "slow-fast" 2ptr approach to solve this in 1 passthrough - O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyHead = ListNode(0, head)       # dummyHead needed for correct distance in this problem
        left = dummyHead
        right = head
        
        while n > 0:                        # create distance of 'n' between 'left' and 'right'
            right = right.next
            n-=1
        
        while right:                        # traverse right to the end of list until NULL
            left = left.next
            right = right.next
        
        left.next = left.next.next          # reroute left.next ptr to get rid of node
        return dummyHead.next