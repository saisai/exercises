package com.mycompany.trees;

public class TreeNode {
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