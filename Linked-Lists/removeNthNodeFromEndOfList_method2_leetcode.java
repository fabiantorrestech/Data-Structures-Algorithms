// problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// TIME: O(n)
// SPACE: O(1)
// - need to traverse list once for size, then again to find node to remove, so O(2n) -> O(n).

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
    
    public int getListSize(ListNode head){
        ListNode curr = head;
        int size = 0;
        while(curr != null){
            curr = curr.next;
            size++;
        }
        return size;
    }
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // - n must be <= size of LL
        
        // want to remove only node in list.
        if((head.next == null && n>0))
            return null;
        
        // get size of LL
        int size = getListSize(head);
        
        // traverse to node to remove.
        // - wherever 'curr' lands, we want to remove from list.
        // - use 'prev' re-route ptrs past 'curr'.
        int numOfNodes = size-n;
        ListNode curr = head;
        ListNode prev = null;
        while(numOfNodes > 0){
            prev = curr;
            curr = curr.next;
            numOfNodes--;
        }
        
        // last node in list is being removed.
        if(curr == null)
            prev.next = null;
        
        // removing head of list
        else if(curr == head)
            head = head.next;
        
        // removing a node in middle of list
        else
            prev.next = curr.next;
        
        return head;
    }
}