package com.mycompany.leetcode.grind75.week3.BinaryTreeLevelOrderTraversal;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeLevelOrderTraversalGfei2 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        levelHelper(res, root, 0);
        return res;
    }

    public void levelHelper(List<List<Integer>> res, TreeNode root, int height) {
        if(root == null) return;
        if(height >= res.size()) {
            res.add(new LinkedList<Integer>());
        }
        res.get(height).add(root.val);
        levelHelper(res, root.left, height + 1);
        levelHelper(res, root.right, height + 1);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20, new TreeNode(15), new TreeNode(7));

        BinaryTreeLevelOrderTraversalGfei2 obj = new BinaryTreeLevelOrderTraversalGfei2();

        List<List<Integer>> results = obj.levelOrder(root);

        results.forEach(list -> {
            System.out.println(list);
        });
    }
}
