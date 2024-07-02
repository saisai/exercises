package com.mycompany.leetcode.TopInterview150.BinaryTreeBFS.BinaryTreeZigzagLevelOrderTraversal;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BinaryTreeZigzagLevelOrderTraversal150awaylu {
    private void travel(TreeNode curr, List<List<Integer>> sol, int level) {
        if(curr == null) return;

        if(sol.size() <= level) {
            List<Integer> newLevel = new LinkedList<>();
            sol.add(newLevel);
        }

        List<Integer> collection = sol.get(level);
        if(level % 2 == 0) collection.add(curr.val);
        else collection.add(0, curr.val);

        travel(curr.left, sol, level + 1);
        travel(curr.right, sol, level + 1);
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root)
    {
        List<List<Integer>> sol = new ArrayList<>();
        travel(root, sol, 0);
        return sol;
    }

    public static void main(String[] args) {

        BinaryTreeZigzagLevelOrderTraversal150awaylu obj = new BinaryTreeZigzagLevelOrderTraversal150awaylu();
        TreeNode root = new TreeNode(3 , new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<List<Integer>> results = obj.zigzagLevelOrder(root);
        results.forEach(lst -> {
            System.out.println(lst);
        });

    }
}
