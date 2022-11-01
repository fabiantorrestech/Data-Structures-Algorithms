#problem: https://leetcode.com/problems/middle-of-the-linked-list/ 
# method 2 -- traverse LL twice (USE MEETHOD 1 if possible)
# TIME: O(n)
# SPACE: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = head
        ptr2 = head
        lengthOfLL = 0
        
        while ptr1 != None:
            ptr1 = ptr1.next
            lengthOfLL+=1
        
        midOfList = lengthOfLL//2
        
        while midOfList > 0:
            ptr2 = ptr2.next
            midOfList-=1
            
        return ptr2