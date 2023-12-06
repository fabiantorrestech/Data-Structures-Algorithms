// problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/ 
// TIME: O(n)
// SPACE: O(1)
// - Optimal Solution. We only need to traverse the list one time total, we can find n'th from end of list by creating 2 pointers: 'left' and 'right'.
// - 'left' will stay at head, then we offset 'right' by n nodes. Now we traverse both pointers until right is at null.
// - 'left' will be at node we want to remove, so we can use a 'prevLeft' pointer to save our node before it. Then, just reroute our 'prevLeft.next' to 'left.next'

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
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // base case: if we are asked to remove nodes, when we have 0 or 1 nodes.
        if((head.next == null && n>0) || head == null)
            return null;
        
        // offset right node first from head by n.
        ListNode right = head;
        while(n>0){
            right = right.next;
            n--;
        }
        
        // now setup left node to be at head.
        // - space between left and right is now 'n' nodes.
        ListNode left = head;
        ListNode prevLeft = null;
        
        // now move both left and right until right is at null
        // - after this, left will be AT NODE we want to delete.
        // - prevLeft is 1 before left, so this will help us reroute our pointers.
        while(right != null){
            prevLeft = left;
            left = left.next;
            right = right.next;
        }
        
        // node to remove is at end of list
        if(left.next == null)
            prevLeft.next = null;
        // node to remove is at begining of list
        else if(left == head)
            head = left.next;
        // node to remove is in middle of list.
        else
            prevLeft.next = left.next;
        
        return head;
        
    }
}
