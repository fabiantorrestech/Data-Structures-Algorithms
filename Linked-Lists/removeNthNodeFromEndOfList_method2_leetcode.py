#problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 
# 2-pass approach, using 3 ptrs. - O(2n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptr1 = head
        ptr2 = head
        prev = head
        sizeOfLL = 0
        
        while ptr1 != None:         # 1) obtains size of LL
            sizeOfLL+=1
            ptr1 = ptr1.next
        
        if n == sizeOfLL:           # Base case: deleting head from LL
            if head.next != None:   # - if head has A next node
                head = head.next
            else:                   # - if head has no next...
                return None
            
        else:
            nodesToPass = sizeOfLL-n
            while nodesToPass > 0:  # 2) find the node to delete
                prev = ptr2
                ptr2 = ptr2.next
                nodesToPass-=1

            if ptr2.next != None:   # - if another node exists after node-to-be-deleted.
                prev.next = ptr2.next
            else:
                prev.next = None    # - if another node DNE after node-to-be-deleted.
    
        return head