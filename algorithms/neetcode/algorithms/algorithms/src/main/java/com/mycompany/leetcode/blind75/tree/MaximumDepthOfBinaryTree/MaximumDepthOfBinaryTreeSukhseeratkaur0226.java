package com.mycompany.leetcode.blind75.tree.MaximumDepthOfBinaryTree;


import com.mycompany.leetcode.blind75.tree.TreeNode;

public class MaximumDepthOfBinaryTreeSukhseeratkaur0226 {
    private static int solve(TreeNode root, int depth){
        if(root == null) return depth;
        int left  = solve(root.left,  depth + 1);
        int right = solve(root.right, depth + 1);
        return Math.max(left, right);
    }
    static int maxDepth(TreeNode root) {
        return solve(root, 0);
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println(maxDepth(root));

    }
}
