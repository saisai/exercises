package com.mycompany.leetcode.grind75.week1.InvertBinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class InvertBinaryTreeJmnarloch {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) {
            return null;
        }

        final TreeNode left = root.left,
                right = root.right;
        root.left = invertTree(right);
        root.right = invertTree(left);
        return root;
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        root.right = new TreeNode(7, new TreeNode(6), new TreeNode(9));

        InvertBinaryTreeJmnarloch obj = new InvertBinaryTreeJmnarloch();
        TreeNode result = obj.invertTree(root);

        new Tree().printInOrder(root);
        System.out.println();
        new Tree().printLevelOrder(root);
    }
}
