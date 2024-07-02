package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.InvertBinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class InvertBinaryTree150PratikSen07 {
    public TreeNode invertTree(TreeNode root) {
        // base case: if the tree is empty
        if(root == null) {
            return root;
        }

        // call the function recursively for the left subtree
        invertTree(root.left);

        // call the function recursively for the right subtree
        invertTree(root.right);

        // swapping process
        TreeNode curr = root.left;
        root.left = root.right;
        root.right = curr;
        return root;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4, new TreeNode(2), new TreeNode(7));
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(9);
        InvertBinaryTree150PratikSen07 obj = new InvertBinaryTree150PratikSen07();
        TreeNode result = obj.invertTree(root);

        new Tree().printInOrder(result);
        
    }
}
