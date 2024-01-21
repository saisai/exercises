package com.mycompany.leetcode.grind75.week8.SerializeAndDeserializeBinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SerializeAndDeserializeBinaryTreeGavinlinasd {
    private static final String spliter = ",";
    private static final String NN = "X";

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if(node == null) {
            sb.append(NN).append(spliter);
        } else {
            sb.append(node.val).append(spliter);
            buildString(node.left, sb);
            buildString(node.right, sb);
        }
    }

    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(spliter)));
        return buildTree(nodes);
    }

    private TreeNode buildTree(Deque<String> nodes) {
        String val = nodes.remove();
        if(val.equals(NN)) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(nodes);
            node.right = buildTree(nodes);
            return node;
        }
    }

    public static void main(String[] args) {
//        String[] root = {"1","2","3","4","5"};
//
//        SerializeAndDeserializeBinaryTreeGavinlinasd obj = new SerializeAndDeserializeBinaryTreeGavinlinasd();
//
//        TreeNode result = obj.deserialize(Arrays.toString(root));

        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        SerializeAndDeserializeBinaryTreeGavinlinasd obj = new SerializeAndDeserializeBinaryTreeGavinlinasd();

        String result = obj.serialize(root);

        System.out.println(result);

    }
}
