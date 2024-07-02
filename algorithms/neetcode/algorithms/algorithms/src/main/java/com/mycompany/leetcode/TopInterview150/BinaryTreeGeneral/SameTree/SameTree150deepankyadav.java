package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.SameTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class SameTree150deepankyadav {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) {
            return true;
        }

        if(p == null || q == null || p.val != q.val) {
            return false;
        }

        // recursively check if the left and right subtrees are identical
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode q = new TreeNode(1, new TreeNode(2), new TreeNode(3));

        SameTree150deepankyadav obj = new SameTree150deepankyadav();
        System.out.println(obj.isSameTree(p, q));
    }
}
