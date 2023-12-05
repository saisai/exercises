package com.mycompany.leetcode.grind75.week1.BalancedBinaryTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class BalancedBinaryTreeTusizi {
    private boolean result = true;

    private int maxDepth(TreeNode root) {
        if(root == null)
            return 0;
        int l = maxDepth(root.left);
        int r = maxDepth(root.right);
        if(Math.abs(l-r) > 1)
            result = false;
        return 1 + Math.max(l, r);
    }

    public boolean isBalanced(TreeNode root) {
        maxDepth(root);
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20, new TreeNode(15), new TreeNode(7));

        BalancedBinaryTreeTusizi obj = new BalancedBinaryTreeTusizi();

        System.out.println(obj.isBalanced(root));
    }
}
