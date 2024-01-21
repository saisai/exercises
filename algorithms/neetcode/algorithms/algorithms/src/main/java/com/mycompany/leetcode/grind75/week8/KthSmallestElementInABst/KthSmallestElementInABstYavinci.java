package com.mycompany.leetcode.grind75.week8.KthSmallestElementInABst;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class KthSmallestElementInABstYavinci {

    int count = 0;
    int result = Integer.MIN_VALUE;
    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(1), new TreeNode(4));
        root.left.right = new TreeNode(2);

        KthSmallestElementInABstYavinci obj = new KthSmallestElementInABstYavinci();
        System.out.println(obj.kthSmallest(root, 1));

    }

    public int kthSmallest(TreeNode root, int k) {
        traverse(root, k);
        return result;
    }

    private void traverse(TreeNode root, int k) {
        if(root == null) {
            return;
        }
        traverse(root.left, k);

        count++;
        if(count == k) {
            result = root.val;
            return;
        }

        traverse(root.right, k);
    }
}
