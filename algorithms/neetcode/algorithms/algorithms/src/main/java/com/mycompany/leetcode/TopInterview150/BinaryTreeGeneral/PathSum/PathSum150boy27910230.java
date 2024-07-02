package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.PathSum;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class PathSum150boy27910230 {
    public boolean hasPathSUm(TreeNode root, int sum) {
        if(root == null) return false;
        if(root.left == null && root.right == null && sum - root.val == 0) {
            return true;
        }

        return hasPathSUm(root.left, sum - root.val) || hasPathSUm(root.right, sum - root.val);
    }

    public static void main(String[] args) {
        PathSum150boy27910230 obj = new PathSum150boy27910230();
        TreeNode root = new TreeNode(5, new TreeNode(4), new TreeNode(8));
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        root.right.left = new TreeNode(13);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(1);

        boolean result = obj.hasPathSUm(root, 22);
        System.out.println(result);
    }
}
