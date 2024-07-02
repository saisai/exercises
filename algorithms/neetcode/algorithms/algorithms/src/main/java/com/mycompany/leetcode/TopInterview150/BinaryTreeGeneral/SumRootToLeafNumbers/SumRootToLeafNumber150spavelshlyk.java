package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.SumRootToLeafNumbers;

import com.mycompany.leetcode.blind75.tree.TreeNode;

public class SumRootToLeafNumber150spavelshlyk {
    public int sum(TreeNode n, int s) {
        if (n == null) return 0;
        if(n.right == null && n.left == null) return s * 10 + n.val;
        return sum(n.left, s*10 + n.val) + sum(n.right, s*10 + n.val);
    }

    public int sumNumbers(TreeNode root) {
        return sum(root, 0);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        SumRootToLeafNumber150spavelshlyk obj = new SumRootToLeafNumber150spavelshlyk();
        int result = obj.sumNumbers(root);
        System.out.println(result);
    }
}
