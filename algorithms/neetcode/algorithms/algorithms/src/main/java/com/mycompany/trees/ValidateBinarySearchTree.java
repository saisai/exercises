package com.mycompany.trees;

public class ValidateBinarySearchTree {
    public static boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        return dfs(root, null, null);
    }

    private static boolean dfs(TreeNode root, Integer min, Integer max) {
        if(root == null) return true;
        if( (min != null && root.getValue() <=min) || max != null && root.getValue() >= max) {
            return false;
        }
        return dfs(root.left, min, root.getValue()) && dfs(root.right, root.getValue(), max);
    }

    public static void main(String... args) {
        TreeNode root = new TreeNode(2);
        root.left = new TreeNode(1);
        root.right = new TreeNode(3);

        System.out.print(isValidBST(root));

    }
}
