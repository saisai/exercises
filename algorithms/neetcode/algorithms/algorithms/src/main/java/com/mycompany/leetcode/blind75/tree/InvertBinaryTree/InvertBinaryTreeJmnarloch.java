package com.mycompany.leetcode.blind75.tree.InvertBinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class InvertBinaryTreeJmnarloch {

    static TreeNode invertTree(TreeNode root) {
        if(root == null) {
            return null;
        }

        final TreeNode left = root.left, right = root.right;
        root.left = invertTree(right);
        root.right = invertTree(left);
        return root;
    }

    static TreeNode invertTreeStack(TreeNode root) {
        if(root == null)
            return null;

        final Deque<TreeNode> stack = new LinkedList<>();
        stack.push(root);

        while(!stack.isEmpty()) {
            final TreeNode node = stack.pop();
            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                stack.push(node.left);
            }

            if(node.right != null) {
                stack.push(node.right);
            }
        }
        return root;
    }

    static TreeNode invertTreeBFS(TreeNode root) {

        if(root == null)
        {
            return null;
        }

        final Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            final TreeNode node = queue.poll();
            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                queue.offer(node.left);
            }

            if(node.right != null) {
                queue.offer(node.right);
            }
        }
        return root;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4, new TreeNode(2), new TreeNode(7));
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(9);

        Tree tree = new Tree();
        tree.printLevelOrder(root);

        System.out.println();
        TreeNode result;
//        result = invertTree(root);
//        result = invertTreeStack(root);
        result = invertTreeBFS(root);
        tree.printLevelOrder(result);
    }
}
