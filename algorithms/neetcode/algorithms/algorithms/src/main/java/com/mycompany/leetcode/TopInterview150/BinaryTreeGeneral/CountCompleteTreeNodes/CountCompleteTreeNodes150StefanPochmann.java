package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.CountCompleteTreeNodes;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class CountCompleteTreeNodes150StefanPochmann {
    int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }
    public int countNodes(TreeNode root) {
        int h = height(root);
        return h < 0 ? 0 :
                height(root.right) == h-1 ? (1 << h) + countNodes(root.right)
                        : (1 << h-1) + countNodes(root.left);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);

        CountCompleteTreeNodes150StefanPochmann obj = new CountCompleteTreeNodes150StefanPochmann();
        System.out.println(obj.countNodes(root));
    }
}
