package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.BinaryTreeMaximumPathSum;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class BinaryTreeMaximumPathSum150weibung {
    int maxValue;

    private int maxPathDown(TreeNode node) {
        if(node == null) return 0;
        int left = Math.max(0, maxPathDown(node.left));
        int right = Math.max(0, maxPathDown(node.right));
        maxValue = Math.max(maxValue, left + right + node.val);
        return Math.max(left, right) + node.val;
    }

    public int maxPathSum(TreeNode root) {
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        BinaryTreeMaximumPathSum150weibung obj = new BinaryTreeMaximumPathSum150weibung();
        System.out.println(obj.maxPathSum(root));
    }

}
