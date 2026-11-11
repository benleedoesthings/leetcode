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
    public boolean findTarget(TreeNode root, int k) {
        return findH(root, k, new HashMap<>());
    }

    private boolean findH(TreeNode root, int k, HashMap<Integer, TreeNode> nodes) {
        if (root == null) return false;

        int complement = k - root.val;
        if (nodes.containsKey(complement)) {
            return true;
        }

        nodes.put(root.val, root);

        return findH(root.left, k, nodes) || findH(root.right, k, nodes); 
    }
}