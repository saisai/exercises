package com.mycompany.leetcode.TopInterview150.BinarySearchTree.ValidateBinarySearchTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class ValidateBinarySearchTree150issac3 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;
        Stack<TreeNode> stack = new Stack<>();
        while(root != null || !stack.empty()) {
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            list.add(root.val);
            root = root.right;
        }
        return list;
    }

    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        while(root != null || !stack.isEmpty()) {
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if(pre != null && root.val <= pre.val) return false;
            pre = root;
            root = root.right;
        }
        return true;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5, new TreeNode(1), new TreeNode(4));
        root.right.left = new TreeNode(3);
        root.right.right = new TreeNode(5);

        ValidateBinarySearchTree150issac3 obj = new ValidateBinarySearchTree150issac3();
        List<Integer> results = obj.inorderTraversal(root);

        results.forEach( data -> {
            System.out.println(data);
        });

        System.out.println(obj.isValidBST(root));
    }
}
