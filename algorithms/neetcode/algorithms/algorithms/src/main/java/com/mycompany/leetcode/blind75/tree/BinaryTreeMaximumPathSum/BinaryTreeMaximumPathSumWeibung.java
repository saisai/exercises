package com.mycompany.leetcode.blind75.tree.BinaryTreeMaximumPathSum;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class BinaryTreeMaximumPathSumWeibung {
    int maxValue;

    public int maxPathSum(TreeNode root) {
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }

    private int maxPathDown(TreeNode node) {
        if(node == null) return 0;
        int left = Math.max(0, maxPathDown(node.left));
        int right = Math.max(0, maxPathDown(node.right));
        maxValue = Math.max(maxValue, left + right + node.val);
        return Math.max(left, right) + node. val;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        new Tree().printInOrder(root);
        System.out.println();
        new Tree().printPostorder(root);
        System.out.println();
        new Tree().printLevelOrder(root);
        System.out.println();
        System.out.println(new BinaryTreeMaximumPathSumWeibung().maxPathSum(root));
        BinaryTreeMaximumPathSumWeibung obj = new BinaryTreeMaximumPathSumWeibung();
        System.out.println(obj.maxPathSum(root));
    }
}
