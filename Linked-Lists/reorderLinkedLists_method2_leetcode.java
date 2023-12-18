// problem: https://leetcode.com/problems/reorder-list/
// - TIME: O(n)
// - SPACE: O(1)
// - Optimal solution. We reverse the 2nd half of LL, cut off the first half but attaching a null pointer to it, then we chain together the nodes via l1.

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
    
    public void printLL(ListNode curr){
        System.out.print("[ ");
        while(curr != null){
            System.out.print( curr.val + " ");
            curr = curr.next;
        }
        System.out.println("]" + "\n");
    }
    
    public ListNode reverseLL(ListNode curr){
        ListNode prev = null;
        ListNode future = null;
        while(curr != null){
            future = curr.next;
            curr.next = prev;
            prev = curr;
            curr = future;
        }
        return prev;
    }
    
    public void chainLists(ListNode l1, ListNode l2){
        // L1 is where we are chaining out nodes into.
       while(l1 != null){
           ListNode l1_future = l1.next;
           ListNode l2_future = l2.next;
           
           l1.next = l2;
           
           // - if the next node in L1 doesn't exist, then we are done. L2's node is the last to be appended.
           // - even if L2 is null, then that marks the end of the list. And if L2 is null, then we cant append null to null.
           if(l1_future == null)
               break;
           
           l2.next = l1_future;
           l1 = l1_future;
           l2 = l2_future;
       }
    }
    
    public void reorderList(ListNode head) {
        // there is nothing to do for a list of LL with size 0 or 1
        if(head == null || head.next == null)
            return;
        
        // get the half of the first list
        ListNode slow = head;
        ListNode preSlow = null;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            preSlow = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        preSlow.next = null;
        
        // reverse 2nd half of LL
        ListNode l2 = reverseLL(slow);
        
        // chain the nodes together into l1
        chainLists(head, l2);
    }
}