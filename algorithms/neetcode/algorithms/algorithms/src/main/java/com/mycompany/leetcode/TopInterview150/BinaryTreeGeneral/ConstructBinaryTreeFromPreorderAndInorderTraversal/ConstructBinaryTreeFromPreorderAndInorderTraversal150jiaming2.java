package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.ConstructBinaryTreeFromPreorderAndInorderTraversal;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class ConstructBinaryTreeFromPreorderAndInorderTraversal150jiaming2 {
    public TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
        if(preStart > preorder.length - 1 || inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = 0;
        for(int i = inStart; i <= inEnd; i++) {
            if(inorder[i] == root.val) {
                inIndex = i;
            }
        }

        root.left = helper(preStart + 1, inStart, inIndex - 1, preorder, inorder);
        root.right = helper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder);
        return root;

    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(0, 0, inorder.length - 1, preorder, inorder);
    }

    public static void main(String[] args) {
//        TreeNode preOrder = new TreeNode(3, new TreeNode(9), new TreeNode(20));
//        preOrder.right.left = new TreeNode(15);
//        preOrder.right.right = new TreeNode(7);
//
//        TreeNode inOrder = new TreeNode(9, new TreeNode(3), new TreeNode(15));
//        inOrder.right.left  = new TreeNode(20);
//        inOrder.right.right = new TreeNode(7);
        int[] preOrder = {3,9,20,15,7};
        int[] inOrder = {9,3,15,20,7};

        ConstructBinaryTreeFromPreorderAndInorderTraversal150jiaming2 obj = new ConstructBinaryTreeFromPreorderAndInorderTraversal150jiaming2();
        TreeNode result = obj.buildTree(preOrder, inOrder);
        new Tree().printInOrder(result);

    }
}
