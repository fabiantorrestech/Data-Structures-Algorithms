// problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// TIME: O(n)
// SPACE: O(1)
// - Need to reverse list once (O(n)),  then find the nth node to delete (can be O(n)), then un-reverse the list (O(n)). 
// - least efficient solution, but easiest to understand.
// - O(3n) -> O(n)

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
    
    public ListNode reverseLL(ListNode head){
        ListNode curr = head;
        ListNode future = null;
        ListNode prev = null;
        while(curr != null){
            future = curr.next;
            curr.next = prev;
            prev = curr;
            curr = future;
        }
        return prev;
    }
    
    public void printLL(ListNode curr){
        System.out.print("[ ");
        while(curr != null){
            System.out.print( curr.val + " ");
            curr = curr.next;
        }
        System.out.println("]" + "\n");
    }
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        if(head.next == null && n>0)
            return null;
        
        // reverse LL
        ListNode reversedLLHead = reverseLL(head);
        
        // traverse 'curr' to n-1'th node from beginning of reversedList
        // - prev will bet at node before 'curr'
        ListNode curr = reversedLLHead;
        ListNode prev = null;
        n = n-1;
        while(n>0){
            prev = curr;
            curr = curr.next;
            n--;
        }
        
        // reroute pointers to skip the n'th node.
        // - if its at beginning of reversedList.
        if(curr == reversedLLHead)
            reversedLLHead = curr.next;
        // - its at the end of reversedList
        else if(curr.next == null){
            prev.next = null;
        }
        // - in the middle of the reversedList.
        else{
            prev.next = curr.next;
        }
        
        // un-reverse the list and return the head.
        head = reverseLL(reversedLLHead);
        return head;
    }
}