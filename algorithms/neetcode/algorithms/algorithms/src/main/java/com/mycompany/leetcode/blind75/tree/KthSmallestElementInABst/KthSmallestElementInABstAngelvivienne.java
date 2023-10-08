package com.mycompany.leetcode.blind75.tree.KthSmallestElementInABst;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Stack;

public class KthSmallestElementInABstAngelvivienne {
    /*
    Binary Search (dfs)
    time complexity: O(N) best, O(N^2) worst
     */
    public int kthSmallestBinarySearchDFS(TreeNode root, int k) {
        int count = countNodes(root.left);
        if(k <= count) {
            return kthSmallestBinarySearchDFS(root.left, k);
        } else if (k > count + 1) {
            return kthSmallestBinarySearchDFS(root.right, k - 1 - count); // // 1 is counted as current node
        }
        return root.val;
    }

    private int countNodes(TreeNode n) {
        if(n == null) return 0;
        return 1 + countNodes(n.left) + countNodes(n.right);
    }


    /*
    DFS in-order recursive:

    time complexity: O(N)
     */
    // better keep these two variables in a wrapper class
    private static int number = 0;
    private static int count = 0;

    public int kthSmallestDFSInOrderRecursive(TreeNode root, int k) {
        count = k;
        helper(root);
        return number;
    }

    private void helper(TreeNode n) {
        if(n.left != null) helper(n.left);
        count--;
        if(count == 0) {
            number = n.val;
            return;
        }
        if(n.right != null) helper(n.right);
    }

    // DFS in-order iterative
    // time complexity: O(N) best
    public int kthSmallestDFSInOrderIterative(TreeNode root, int k) {
        Stack<TreeNode> st = new Stack<>();

        while(root != null) {
            st.push(root);
            root = root.left;
        }

        while(k != 0) {
            TreeNode n = st.pop();
            k--;
            if(k == 0) return n.val;
            TreeNode right = n.right;
            while(right != null) {
                st.push(right);
                right = right.left;
            }
        }
        return -1; // never hit if k is valid
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(1), new TreeNode(4));
        root.left.right = new TreeNode(2);
        final int k = 1;

        KthSmallestElementInABstAngelvivienne obj = new KthSmallestElementInABstAngelvivienne();
        int result = obj.kthSmallestBinarySearchDFS(root, k);
        System.out.println(result);

        int result2 = obj.kthSmallestDFSInOrderRecursive(root, k);
        System.out.println(result2);

        int result3 = obj.kthSmallestDFSInOrderIterative(root, k);
        System.out.println(result3);
    }
}
