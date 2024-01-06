package com.mycompany.leetcode.grind75.week6.ConstructBinaryTreeFromPreorderAndInorderTraversal;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class ConstructBinaryTreeFromPreorderAndInorderTraversalJaming2 {
    public TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder){
        if(preStart > preorder.length - 1 || inStart > inEnd) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = 0; // index of current root in inorder
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
        int[] preorder = {3,9,20,15,7}, inorder = {9,3,15,20,7};

        ConstructBinaryTreeFromPreorderAndInorderTraversalJaming2 obj = new ConstructBinaryTreeFromPreorderAndInorderTraversalJaming2();
        TreeNode root = obj.buildTree(preorder, inorder);

        new Tree().printLevelOrder(root);
    }
}
