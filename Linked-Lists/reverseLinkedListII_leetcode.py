# problem: https://leetcode.com/problems/reverse-linked-list-ii/
# - TIME: O(n), where is number of all nodes in linked list.
# - SPACE: O(1) no extra space required that will scale.
#   - utilizes dummyHead, and strategic pointer placement.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:       # Base Case: the numnber of nodes to reroute 'next' ptrs = 0
            return head
        
        dummyHead = ListNode(0, head)
        prevLeftNode, curr = dummyHead, head
        
        for i in range(left-1):         # traverse 2 ptrs: prevLN & curr (leftNode)
            prevLeftNode, curr = curr, curr.next
        
        prev = None
        for i in range(right-left+1):   # reverse 'left' to 'right' nodes.
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        
        prevLeftNode.next.next = curr   # curr is at 1 after rightNode so we can link to rest of list.
        prevLeftNode.next = prev        # prevLeftNode.next -> rightNode .. -> prev -> rest of List

        return dummyHead.next           # return head of entire modified list.