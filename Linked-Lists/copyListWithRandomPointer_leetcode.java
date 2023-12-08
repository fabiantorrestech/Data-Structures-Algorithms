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
        
        // use original nodes as keys to reach deepCopies of original nodes. <k,v> -> <originalNode, deepCopyNode>
        HashMap<Node, Node> originalToNew = new HashMap<Node, Node>();
        
        // create new nodes
        Node curr = head;
        while(curr != null){
            Node temp = new Node(curr.val);
            originalToNew.put(curr, temp);
            curr = curr.next;
        }
        
        // use hashmap of <originalNode, deepCopyNode> to reach deepCopyNode.
        // - we can then find the exact nodes that correspond to random and next pointers for deepcopy because this is 1:1 copy.
        // + deepCopyNode.next = hm.get(originalNode.next);
        // + deepCopyNode.random = hm.get(deepCopyNode.random);
        curr = head;
        Node copyCurr = originalToNew.get(curr);
        Node copyHead = null;
        while(curr != null){
            // need a reference to the head of deepCopy LL.
            if(copyHead == null)
                copyHead = copyCurr;
            
            // use original node references to get copies to next and random references in new list.
            copyCurr.next = originalToNew.get(curr.next);
            copyCurr.random = originalToNew.get(curr.random);
            
            // remember to increment original and deepCopy list nodes
            copyCurr = copyCurr.next;
            curr = curr.next;
        }
        
        return copyHead;
    }
}