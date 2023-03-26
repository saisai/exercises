package com.mycompany.trees;

import javafx.util.Pair;

public class BalancedBinaryTree {

    public static void main(String... args) {

    }

    private static Pair<Boolean, Integer> dfs(TreeNode root) {
        if(root == null) {
            return new Pair<Boolean, Integer>(true, 0);
        }

        Pair<Boolean, Integer> left = dfs(root.left);
        Pair<Boolean, Integer> right = dfs(root.right);

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
