package com.mycompany.leetcode.grind75.week2.DiameterOfBinaryTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class DiameterOfBinaryTreeShawngao {
    int max = 0;

    private int maxDepth(TreeNode root) {
        if(root == null) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        max = Math.max(max, left + right);
        return Math.max(left, right) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return max;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(6);

        DiameterOfBinaryTreeShawngao obj = new DiameterOfBinaryTreeShawngao();
        int result = obj.diameterOfBinaryTree(root);
        System.out.println(result);

    }
}
