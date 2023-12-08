// problem:  https://leetcode.com/problems/add-two-numbers/
// TIME: O(n)
// SPACE: O(n)
// - almost the most optimal solution, but very messy. need to create a whole new list of size n+1 at most, where n = num of nodes in l1 + num of nodes in l2.
// - n+1 because we may have a carry up until the last digit, where we may need to create a brand new node for it. 


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
     // handles carry for rest of digits in 1 list.
    public ListNode handleCarry(ListNode l1, int carry){
        ListNode l1_head = l1;
        ListNode l1_prev = l1;
        
        while(l1 != null){
            l1_prev = l1;
            l1.val += carry;
            carry = 0;
            if(l1.val>=10){
                l1.val-=10;
                carry=1;
            }
            l1 = l1.next;
        }
        
        // we are left with a carry at the very last digit, but have no node in current list to add the carry to.
        if(carry > 0 && l1 == null){
            // there is a previous node in current list we can add the carry to.
            if(l1_prev != null){
                l1_prev.next = new ListNode(carry);
                carry = 0;
            }
            // l1 and l2 are both null, but have a carry from its last digits' sum.
            else
                return new ListNode(carry);
        }
        
        return l1_head;
    }
    
    public ListNode addDigits(ListNode l1, ListNode l2, int carry){
        
        // base cases:
        // - all must account for case where we have traversed entire list and have carry OR no carry.
        if(l1 != null && l2 == null){
            if(carry > 0)
                return handleCarry(l1, carry);
            else
                return l1;   
        }
        else if(l1 == null && l2 != null){
            if(carry > 0)
                return handleCarry(l2, carry);
            else
                return l2;
        }
        else if(l1 == null && l2 == null)
            if(carry > 0)
                return handleCarry(l1, carry);
            else
                return null;
        
        ListNode curr = new ListNode(l1.val + l2.val + carry);
        // if there is carry, take it into account for next digits in lists' addDigits recursive-call.
        if(curr.val>=10){
            curr.val-=10;
            curr.next = addDigits(l1.next, l2.next, 1);
        }
        // no carry
        else
            curr.next = addDigits(l1.next, l2.next, 0);
        
        return curr;
    }   
    
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        // initialize dummmy node
        ListNode ansHead = new ListNode(0);
        ansHead.next = addDigits(l1, l2, 0);
        
        return ansHead.next;
    }
}