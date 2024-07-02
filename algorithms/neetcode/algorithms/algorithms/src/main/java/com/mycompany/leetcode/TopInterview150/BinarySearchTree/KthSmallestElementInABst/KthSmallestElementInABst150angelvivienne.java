package com.mycompany.leetcode.TopInterview150.BinarySearchTree.KthSmallestElementInABst;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class KthSmallestElementInABst150angelvivienne {
    private int countNodes(TreeNode n) {
        if(n == null) return 0;
        return 1 + countNodes(n.left) + countNodes(n.right);
    }

    public int kthSmallest(TreeNode root, int k) {
        int count = countNodes(root.left);
        if(k <= count) {
            return kthSmallest(root.left, k);
        } else if( k > count + 1) {
            return kthSmallest(root.right, k-1-count);
        }

        return root.val;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(1), new TreeNode(4));
        root.left.right = new TreeNode(2);

        KthSmallestElementInABst150angelvivienne obj = new KthSmallestElementInABst150angelvivienne();
        int result = obj.kthSmallest(root, 1);
        System.out.println(result);
    }
}
