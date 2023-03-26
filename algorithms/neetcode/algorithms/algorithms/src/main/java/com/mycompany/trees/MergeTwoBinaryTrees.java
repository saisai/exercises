package com.mycompany.trees;
public class MergeTwoBinaryTrees {
    public static TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return null;

        int val1 = root1 != null ? root1.getValue() : 0;
        int val2 = root2 != null ? root2.getValue() : 0;

        TreeNode root = new TreeNode(val1 + val2);

        // merge left side of trees if they are not null
        root.left =
                mergeTrees(
                        (root1 != null && root1.left != null) ? root1.left : null,
                        (root2 != null && root2.left != null) ? root2.left : null
                );

        // merge righ side of trees if they are not null
        root.right =
                mergeTrees(
                        (root1 != null && root1.right != null) ? root1.right : null,
                        (root2 != null && root2.right != null) ? root2.right : null
                );

        return root;
    }

    public static void main(String... args) {
        //root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]

        TreeNode root1 = new TreeNode(1, null, null);
        root1.left = new TreeNode(3, null, null);
        root1.right = new TreeNode(2, null, null);
        root1.left.left = new TreeNode(5, null, null);

        TreeNode root2 = new TreeNode(2, null, null);
        root2.left = new TreeNode(1, null, null);
        root2.left.right = new TreeNode(4, null, null);
        root2.right = new TreeNode(3, null, null);
        root2.right.right = new TreeNode(7, null, null);

        TreeNode result = mergeTrees(root1, root2);


    }
}
