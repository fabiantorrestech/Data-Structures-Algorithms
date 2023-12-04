// problem: https://leetcode.com/problems/invert-binary-tree/
// TIME: O(n)
// SPACE: O(logn) - 1 stack frame for each level, so you would logn frames at deepest depth.
// - Recursive DFS solution in Java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public TreeNode invertTree(TreeNode root) {
        
        // recursive base case
        if(root == null)
            return null;
        
        // swap left and right using a temp TreeNode and recursion
        if(root.left != null || root.right != null){
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
            invertTree(root.left);
            invertTree(root.right);
        }
        
        return root;
        
    }
}