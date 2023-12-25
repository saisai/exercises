package com.mycompany.leetcode.grind75.week5.LowestCommonAncestorOfABinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.*;

public class LowestCommonAncestorOfABinaryTreeIssac3 {
    public TreeNode lowestCommonAncestor(TreeNode  root, TreeNode p, TreeNode q) {
        if(root == null) return null;
        if(root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        return left != null && right != null ? root : left == null ? right : left;
    }

    public static void main(String[] args) {
        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4)));
        root.right = new TreeNode(1, new TreeNode(0), new TreeNode(8));

        LowestCommonAncestorOfABinaryTreeIssac3 obj = new LowestCommonAncestorOfABinaryTreeIssac3();
        TreeNode result = obj.lowestCommonAncestor(root, p, q);
        Tree r = new Tree();
        r.printInOrder(result);

    }


}
