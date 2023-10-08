package com.mycompany.leetcode.blind75.tree.SubtreeOfAnotherTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class SubtreeOfAnotherTreeShawngao {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s == null) return false;
        if(isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }

    private boolean isSame(TreeNode s, TreeNode t) {
        if(s == null && t == null) return true;
        if(s == null || t == null) return false;

        if(s.val != t.val) return false;

        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(4), new TreeNode(5));
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(2);

        TreeNode subRoot = new TreeNode(4, new TreeNode(1), new TreeNode(2));

        SubtreeOfAnotherTreeShawngao obj = new SubtreeOfAnotherTreeShawngao();
        System.out.println(obj.isSubtree(root, subRoot));
    }
}
