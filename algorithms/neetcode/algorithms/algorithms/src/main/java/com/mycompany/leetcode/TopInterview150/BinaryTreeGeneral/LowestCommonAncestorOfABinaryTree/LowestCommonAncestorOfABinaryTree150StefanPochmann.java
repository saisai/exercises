package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.LowestCommonAncestorOfABinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class LowestCommonAncestorOfABinaryTree150StefanPochmann {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        return left == null ? right : right == null ? left : root;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(5), new TreeNode(1));
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);
        root.left.right.left = new TreeNode(7);
        root.left.right.right = new TreeNode(4);

        root.right.left = new TreeNode(0);
        root.right.right = new TreeNode(8);

        LowestCommonAncestorOfABinaryTree150StefanPochmann obj = new LowestCommonAncestorOfABinaryTree150StefanPochmann();
        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);
        TreeNode result = obj.lowestCommonAncestor(root, p, q);

        new Tree().printInOrder(result);

    }
}
