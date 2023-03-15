package com.mycompany.trees;

import javafx.util.Pair;

class TreeNode {
     int value;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int value) { this.value = value; }
     TreeNode(int value, TreeNode left, TreeNode right) {
         this.value = value;
         this.left = left;
         this.right = right;
     }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}

public class BalancedBinaryTree {

    public static void main(String... args) {

    }

    private static Pair<Boolean, Integer> dfs(TreeNode root) {
        if(root == null) {
            return new Pair<Boolean, Integer>(true, 0);
        }

        int left = dfs(root.left);
        int right = dfs(root.right);

        boolean balanced = left.getKey() &&
                right.getKey() &&
                (Math.abs(left.getValue() - right.getValue()) <= 1);

        return new Pair<Boolean, Integer>(
                balanced,
                1 + Math.max(left.getValue(), right.getValue())
        );

    }

    public static boolean isBalanced(TreeNode root) {
        return dfs(root).getKey();
    }

}
