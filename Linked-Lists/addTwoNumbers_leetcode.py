# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy                    # create a new list to store the values. 
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            ans = val1 + val2 + carry
            carry = ans//10             # will only be non-zero if "ans > 9"
            ans = ans%10                # will store the 1's value of 'ans' in current node. 
            curr.next = ListNode(ans)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        # if we have exhausted both lists and we still have a carry, make an extra node to store the carry
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next