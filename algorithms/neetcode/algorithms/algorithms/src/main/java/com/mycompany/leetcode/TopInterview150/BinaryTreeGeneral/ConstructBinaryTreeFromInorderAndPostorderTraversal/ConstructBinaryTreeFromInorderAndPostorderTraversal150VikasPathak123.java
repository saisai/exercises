package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.ConstructBinaryTreeFromInorderAndPostorderTraversal;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class ConstructBinaryTreeFromInorderAndPostorderTraversal150VikasPathak123 {
    private TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postOrder, int postStart, int postEnd) {
        // base case
        if(inStart > inEnd || postStart > postEnd)
        {
            return null;
        }

        // find the root node from the last element of postorder traversal
        int rootVal = postOrder[postEnd];
        TreeNode root = new TreeNode(rootVal);

        // find the index of the root node in inorder traversal
        int rootIndex = 0;
        for(int i = inStart; i <= inEnd; i++) {
            if(inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        // Recursively build the left and right subtrees
        int leftSize = rootIndex - inStart;
        int rightSize = inEnd - rootIndex;
        root.left = buildTree(inorder, inStart, rootIndex - 1, postOrder, postStart, postStart + leftSize - 1);
        root.right = buildTree(inorder, rootIndex + 1, inEnd, postOrder, postEnd - rightSize, postEnd - 1);

        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // Call the recursive function with full arrays and return the result
        return buildTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
    }

    public static void main(String[] args) {
        int inorder[] = {9,3,15,20,7}, postorder[] = {9,15,7,20,3};
        ConstructBinaryTreeFromInorderAndPostorderTraversal150VikasPathak123 obj = new ConstructBinaryTreeFromInorderAndPostorderTraversal150VikasPathak123();
        TreeNode result = obj.buildTree(inorder, postorder);
        new Tree().printInOrder(result);
    }
}
