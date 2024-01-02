package com.mycompany.leetcode.grind75.week6.BinaryTreeRightSideView;

import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeRightSideViewZwangbo {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        rightView(root, result, 0);
        return result;
    }

    private void rightView(TreeNode curr, List<Integer> result, int currDepth) {
        if(curr == null) {
            return;
        }

        if(currDepth == result.size()) {
            result.add(curr.val);
        }

        rightView(curr.left, result, currDepth + 1);
        rightView(curr.right, result, currDepth + 1);
    }

    public static void main(String[] args) {
        TreeNode root  = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(4);
        BinaryTreeRightSideViewZwangbo obj = new BinaryTreeRightSideViewZwangbo();
        List<Integer> results = obj.rightSideView(root);

        results.forEach(lst -> {
            System.out.print(lst);
        });
    }
}
