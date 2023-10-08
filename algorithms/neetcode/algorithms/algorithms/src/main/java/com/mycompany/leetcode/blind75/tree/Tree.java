package com.mycompany.leetcode.blind75.tree;

public class Tree {

    // https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    public void printInOrder(TreeNode root) {
        if(root == null) {
            return;
        }

        // first recur on left child
        printInOrder(root.left);

        // print the val of node
        System.out.print(root.val + " ");

        // recur on right child
        printInOrder(root.right);
    }

    public void printPreorder(TreeNode root) {
        if(root == null) {
            return;
        }

        // print the val of node
        System.out.print(root.val + " ");

        // first recur on left child
        printPreorder(root.left);

        // recur on right child
        printPreorder(root.right);
    }


    public void printPostorder(TreeNode root) {
        if(root == null) {
            return;
        }


        // first recur on left child
        printPostorder(root.left);

        // recur on right child
        printPostorder(root.right);

        // print the val of node
        System.out.print(root.val + " ");
    }


    // Level Order Traversal (Naive approach):
    // https://www.geeksforgeeks.org/level-order-tree-traversal/
    // Function to print level order traversal of tree
    public void printLevelOrder(TreeNode root)
    {
        int h = height(root);
        int i;
        for (i = 1; i <= h; i++)
            printCurrentLevel(root, i);
    }

    // Compute the "height" of a tree -- the number of
    // nodes along the longest path from the root node
    // down to the farthest leaf node.
    private int height(TreeNode root)
    {
        if (root == null)
            return 0;
        else {

            // Compute  height of each subtree
            int lheight = height(root.left);
            int rheight = height(root.right);

            // use the larger one
            if (lheight > rheight)
                return (lheight + 1);
            else
                return (rheight + 1);
        }
    }

    // Print nodes at the current level
    private void printCurrentLevel(TreeNode root, int level)
    {
        if (root == null)
            return;
        if (level == 1)
            System.out.print(root.val + " ");
        else if (level > 1) {
            printCurrentLevel(root.left, level - 1);
            printCurrentLevel(root.right, level - 1);
        }
    }
}

// https://www.javatpoint.com/tree-traversal
// https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
