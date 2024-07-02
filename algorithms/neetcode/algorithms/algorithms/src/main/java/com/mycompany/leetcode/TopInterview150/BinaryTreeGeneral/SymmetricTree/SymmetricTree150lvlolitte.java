package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.SymmetricTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class SymmetricTree150lvlolitte {
    public boolean isSymmetric(TreeNode root) {
        return root == null || isSymmetricHelp(root.left, root.right);
    }

    private boolean isSymmetricHelp(TreeNode left, TreeNode right) {
        if(left == null || right ==null)
            return left == right;
        if(left.val != right.val)
            return false;
        return isSymmetricHelp(left.left, right.right) &&
        isSymmetricHelp(left.right, right.left);

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(2));
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(3);

        SymmetricTree150lvlolitte obj = new SymmetricTree150lvlolitte();
        System.out.println(obj.isSymmetric(root));
    }


}
