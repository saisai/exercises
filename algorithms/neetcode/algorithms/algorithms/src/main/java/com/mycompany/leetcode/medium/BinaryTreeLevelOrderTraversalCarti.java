package com.mycompany.leetcode.medium;

import com.mycompany.leetcode.TreeNode;

import java.util.*;

public class BinaryTreeLevelOrderTraversalCarti {
    private static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        // handle edge case; root is orginally empty
        if(root == null) return result;
        // queue for bfs
        Queue<TreeNode> queue = new LinkedList(){{ add(root); }};

        // go until queue is empty (there are still levels)
        while(!queue.isEmpty()) {
            // get size of this level, and array to hold current level's vals
            int size = queue.size();
            List<Integer> currentLevel = new ArrayList<>();

            while(size-- > 0) {
                // popleft, and add val to current level
                TreeNode current = queue.poll();
                currentLevel.add(current.val);

                // add children (which are next level)
                if(current.left != null) queue.add(current.left);
                if(current.right != null) queue.add(current.right);
            }

            // we're finished with this level, onto the next level
            result.add(currentLevel);
        }
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<List<Integer>> results = levelOrder(root);

        System.out.println(Arrays.toString(results.toArray()));

    }
}
