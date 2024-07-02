package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.BinarySearchTreeIterator;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Stack;

public class BinarySearchTreeIterator150xcv58 {
    private Stack<TreeNode> stack = new Stack<TreeNode>();

    private void pushAll(TreeNode node) {
        for(; node != null; stack.push(node), node = node.left);
    }
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode tmpNode = stack.pop();
        pushAll(tmpNode.right);
        return tmpNode.val;
    }
    BinarySearchTreeIterator150xcv58(TreeNode root) {
        pushAll(root);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(7, new TreeNode(3), new TreeNode(15));
        root.right.left = new TreeNode(9);
        root.right.right = new TreeNode(20);
        BinarySearchTreeIterator150xcv58 bSTIterator = new BinarySearchTreeIterator150xcv58(root);
        bSTIterator.next();    // return 3
        bSTIterator.next();    // return 7
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 9
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 15
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 20
        bSTIterator.hasNext(); // return False
    }
}
