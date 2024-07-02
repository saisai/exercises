package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.FlattenBinaryTreeToLinkedList;

import com.mycompany.leetcode.blind75.tree.TreeNode;
import com.mycompany.leetcode.blind75.tree.Tree;

public class FlattenBinaryTreeToLinkedList150tusizi {
    private TreeNode prev = null;

    public void flatten(TreeNode root) {
        if(root == null)
            return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)), new TreeNode(5));
        root.right.right = new TreeNode(6);
        FlattenBinaryTreeToLinkedList150tusizi obj = new FlattenBinaryTreeToLinkedList150tusizi();
        new Tree().printInOrder(root);
    }
}
