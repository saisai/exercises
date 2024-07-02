package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.MaximumDepthOfBinaryTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Stack;

public class MaximumDepthOfBinaryTree150yfcheng {
    public int maxDepth(TreeNode  root) {
        if(root == null) {
            return 0;
        }

        Stack<TreeNode> stack = new Stack<>();
        Stack<Integer> value = new Stack<>();
        stack.push(root);
        value.push(1);
        int max = 0;
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            int temp = value.pop();
            max = Math.max(temp, max);
            if(node.left != null) {
                stack.push(node.left);
                value.push(temp+1);
            }
            if(node.right != null) {
                stack.push(node.right);
                value.push(temp+1);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        MaximumDepthOfBinaryTree150yfcheng obj = new MaximumDepthOfBinaryTree150yfcheng();
        int result = obj.maxDepth(root);
        System.out.println(result);

    }
}
