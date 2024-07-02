package com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.PopulatingNextRightPointersInEachNodeIi;

import com.mycompany.leetcode.TopInterview150.BinaryTreeGeneral.Node;
import com.mycompany.leetcode.blind75.tree.TreeNode;

public class PopulatingNextRightPointersInEachNodeIi150davidtan1890 {
    public void connect(Node root) {
        while(root != null) {
            Node tempChild = new Node(0);
            Node currentChild = tempChild;
            while(root != null) {
                if(root.left != null) { currentChild.next = root.left; currentChild = currentChild.next;}
                if(root.right != null) { currentChild.next = root.right; currentChild = currentChild.next;}
                root = root.next;
            }
            root = tempChild.next;
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(7);

        PopulatingNextRightPointersInEachNodeIi150davidtan1890 obj = new PopulatingNextRightPointersInEachNodeIi150davidtan1890();
//        Node resul = obj.connect(root);
    }
}
