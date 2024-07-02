package com.mycompany.leetcode.TopInterview150.BinaryTreeBFS.BinaryTreeLevelOrderTraversal;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeLevelOrderTraversal150Soy {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();

        if(root == null) return wrapList;

        queue.offer(root);
        while(!queue.isEmpty()) {
            int levelNum = queue.size();
            List<Integer> subList = new LinkedList<Integer>();
            for(int i=0; i < levelNum; i++) {
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                subList.add(queue.poll().val);
            }
            wrapList.add(subList);
        }
        return wrapList;
    }

    public static void main(String[] args) {
        BinaryTreeLevelOrderTraversal150Soy obj = new BinaryTreeLevelOrderTraversal150Soy();
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20));
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<List<Integer>> results = obj.levelOrder(root);
        results.forEach(data -> {
            System.out.println(data);
        });


    }
}
