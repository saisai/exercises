package com.mycompany.leetcode.grind75.week1.LowestCommonAncestorOfABinarySearchTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class LowestCommonAncestorOfABinarySearchTreeChrisTJZ {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if(root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(6);
        root.left = new TreeNode(2, new TreeNode(0), new TreeNode(4, new TreeNode(3), new TreeNode(5)));
        root.right = new TreeNode(8, new TreeNode(7), new TreeNode(9));
        TreeNode p = new TreeNode(2);
        TreeNode q = new TreeNode(8);

        LowestCommonAncestorOfABinarySearchTreeChrisTJZ obj = new LowestCommonAncestorOfABinarySearchTreeChrisTJZ();
        TreeNode result = obj.lowestCommonAncestor(root, p, q);

        new Tree().printLevelOrder(result);

    }
}
