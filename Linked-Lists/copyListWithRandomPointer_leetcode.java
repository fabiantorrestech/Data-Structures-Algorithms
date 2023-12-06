// problem: https://leetcode.com/problems/copy-list-with-random-pointer/
// TIME: O(n)
// SPACE: O(n)
// - Optimal solution with 2 passes of original list. 1 pass to populate hashtable and new nodes for deepcopy list.
// - 1 pass to link each deepcopy node's random and next pointers, utilizing the hashmap. O(2n) -> O(n) 

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    
    public Node copyRandomList(Node head) {
        
        HashMap<Node, Node> originalToCopy = new HashMap<Node, Node>();
        
        // link original nodes to deepcopy nodes
        Node curr = head;
        while(curr != null){
            Node temp = new Node(curr.val);
            originalToCopy.put(curr, temp);
            curr = curr.next;
        }
        
        curr = head;
        Node headCopy = originalToCopy.get(curr);
        Node currCopy = headCopy;
        while(curr != null){
            currCopy.next = originalToCopy.get(curr.next);
            currCopy.random = originalToCopy.get(curr.random);
            currCopy = currCopy.next;
            curr = curr.next;
        }
        
        return headCopy;
    }
}