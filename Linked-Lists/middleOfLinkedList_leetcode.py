#problem: https://leetcode.com/problems/middle-of-the-linked-list/ 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head != None:
            numNodes = 0
            ptr1 = head
            ptr2 = head             
            
            while ptr1 != None:     # 1) get the LL length using 1 ptr
                numNodes += 1
                ptr1 = ptr1.next
            
            midOfList = numNodes//2
            
            while midOfList > 0:    # 2) traverse to the middle of the list by using middle (derived above)
                ptr2 = ptr2.next
                midOfList -= 1
            
            return ptr2
        
        return None