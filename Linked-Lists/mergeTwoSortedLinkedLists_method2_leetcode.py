# problem: https://leetcode.com/problems/merge-two-sorted-lists/
# still optimal solution, but not very clean... No dummy head utilized. (check method1 for more elegant clean solution.)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 and not list2) or (not list1 and list2):
            return list1 if list1 else list2
        
        p1, p2, newHead, newCurr = list1, list2, None, None
        
        while p1 and p2:
            print("p1: ", p1.val, " / p2: ", p2.val)
            
            if newHead == None:         # intializing the newHead to return
                if p1.val <= p2.val:
                    newHead = p1
                    p1 = p1.next
                    newCurr = newHead
                else:
                    newHead = p2
                    p2 = p2.next
                    newCurr = newHead
            
            else:
                if p1.val <= p2.val:
                    temp = p1
                    p1 = p1.next
                elif p1.val > p2.val:
                    temp = p2
                    p2 = p2.next
                newCurr.next = temp
                newCurr = newCurr.next
                
        if p1 or p2:
            newCurr.next = p1 if p1 else p2 
        
        return newHead