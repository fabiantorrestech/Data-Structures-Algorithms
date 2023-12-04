// problem: https://leetcode.com/problems/merge-two-sorted-lists/
// TIME: O(n)
// SPACE: O(1)
// - Optimal solution, implemented in Java

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
    
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        // create a dummy head.
        ListNode head = new ListNode(0, null);
        ListNode curr = head;
        
        // while both lists are not empty, look for the smaller value of each LL
        while(list1 != null && list2 != null){
            if(list2.val >= list1.val){
                curr.next = list1;
                list1 = list1.next;
            }
            else if(list1.val > list2.val){
                curr.next = list2;
                list2 = list2.next;
            }
            curr = curr.next;
        }
        
        // populate the rest of the LL with whichever list is not yet empty.
        if(list1 == null && list2 != null)
            curr.next = list2;
        else if(list2 == null && list1 != null)
            curr.next = list1;
        
        return head.next;
    }
}