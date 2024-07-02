package com.mycompany.leetcode.TopInterview150.BinarySearchTree.MinimumAbsoluteDifferenceInBst;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class MinimumAbsoluteDifferenceInBst150shawngao {
    int min = Integer.MAX_VALUE;
    Integer prev = null;

    public int getMinimumDifference(TreeNode root) {
        if(root == null) return min;

        getMinimumDifference(root.left);

        if(prev != null) {
            min = Math.min(min, root.val - prev);
        }

        prev = root.val;

        getMinimumDifference(root.right);

        return min;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4, new TreeNode(2), new TreeNode(6));
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        MinimumAbsoluteDifferenceInBst150shawngao obj = new MinimumAbsoluteDifferenceInBst150shawngao();
        System.out.println(obj.getMinimumDifference(root));
    }
}
