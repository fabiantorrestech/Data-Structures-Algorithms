// problem: https://leetcode.com/problems/reverse-linked-list/
// TIME: O(n)
// SPACE: O(1)
// - Most optimal solution for reversing a linked list implemented in Java!

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
    
    void printList(ListNode curr){
        while(curr != null){
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
        System.out.println();
    }
    
    public ListNode reverseList(ListNode head) {
        // printList(head);
        ListNode curr = head;
        ListNode prev = null;
        ListNode future = null;
        while(curr != null){
            future = curr.next;
            curr.next = prev;
            prev = curr;
            curr = future;
        }
        // printList(prev);
        return prev;
    }
}