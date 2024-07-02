package com.mycompany.leetcode.TopInterview150.BinaryTreeBFS.AverageOfLevelsInBinaryTree;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class AverageOfLevelsInBinaryTree150Earlme {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new ArrayList<>();
        Queue<TreeNode> q  = new LinkedList<>();

        if(root == null) return result;
        q.add(root);
        while(!q.isEmpty()) {
            int n = q.size();
            double sum = 0.0;
            for(int i = 0; i < n; i++) {
                TreeNode node = q.poll();
                sum += node.val;
                if(node.left != null) q.offer(node.left);
                if(node.right != null) q.offer(node.right);
            }
            result.add(sum / n);
        }
        return result;
    }

    public static void main(String[] args) {
        AverageOfLevelsInBinaryTree150Earlme obj = new AverageOfLevelsInBinaryTree150Earlme();
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<Double> results = obj.averageOfLevels(root);

        for(Double dd : results) {
            System.out.println(dd);
        }
    }
}
