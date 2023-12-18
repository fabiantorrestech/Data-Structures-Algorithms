// problem: https://leetcode.com/problems/linked-list-cycle/
// TIME: O(logn)
// SPACE: O(1)
// - Optimal solution. Takes logn time because slow moves at normal speed and fast moves 2x faster than slow skipping some nodes.
// - so fast will either get to end of list (if no cycle exists) OR fast will overlap back to slow. if fast meets slow, then there is a cycle.

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast)
                return true;
        }
        return false;
    }
}