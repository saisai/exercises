package com.mycompany.leetcode.TopInterview150.BinaryTreeBFS.BinaryTreeRightSideView;

import com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.BinarySearchTreeIterator.BinarySearchTreeIterator150xcv58;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeRightSideView150zwangbo {
    public void rightView(TreeNode  curr, List<Integer> result, int currDepth) {
        if(curr == null) {
            return;
        }
        if(currDepth == result.size()) {
            result.add(curr.val);
        }

        rightView(curr.right, result, currDepth + 1);
        rightView(curr.left, result, currDepth + 1);
    }

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        rightView(root, result, 0);
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(4);

        BinaryTreeRightSideView150zwangbo obj = new BinaryTreeRightSideView150zwangbo();
        List<Integer> results = obj.rightSideView(root);

        for(Integer obj2 : results) {
            System.out.println(obj2);
        }

    }
}
