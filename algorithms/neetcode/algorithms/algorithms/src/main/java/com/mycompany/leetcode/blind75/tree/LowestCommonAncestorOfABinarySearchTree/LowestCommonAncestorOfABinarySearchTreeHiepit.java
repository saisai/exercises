package com.mycompany.leetcode.blind75.tree.LowestCommonAncestorOfABinarySearchTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class LowestCommonAncestorOfABinarySearchTreeHiepit {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p,  TreeNode q) {
        int small = Math.min(p.val, q.val);
        int large = Math.max(p.val, q.val);
        System.out.println(small);
        System.out.println(large);
        while(root != null) {
            if(root.val > large)
                root = root.left;
            else if(root.val < small)
                root = root.right;
            else
                return root;
        }
        return null;
    }

    public static void main(String[] args) {

//        TreeNode root = new TreeNode(6, new TreeNode(2), new TreeNode(8));
//        root.left.left = new TreeNode(0);
//        root.left.right = new TreeNode(4, new TreeNode(3), new TreeNode(5));
//        root.right.left = new TreeNode(8, new TreeNode(7), new TreeNode(9));
//        new Tree().printInOrder(root);
//        System.out.println();
//        new Tree().printLevelOrder(root);
//        System.out.println();

        TreeNode root2 = new TreeNode(6);
        root2.left = new TreeNode(2, new TreeNode(0), new TreeNode(4, new TreeNode(3), new TreeNode(5)));
        root2.right = new TreeNode(8, new TreeNode(7), new  TreeNode(9));

        TreeNode p = new TreeNode(2);
        TreeNode q = new TreeNode(8);
        new Tree().printLevelOrder(root2);
        System.out.println();
        LowestCommonAncestorOfABinarySearchTreeHiepit obj = new LowestCommonAncestorOfABinarySearchTreeHiepit();
        TreeNode result = obj.lowestCommonAncestor(root2, p, q);

        new Tree().printInOrder(result);
    }
}
