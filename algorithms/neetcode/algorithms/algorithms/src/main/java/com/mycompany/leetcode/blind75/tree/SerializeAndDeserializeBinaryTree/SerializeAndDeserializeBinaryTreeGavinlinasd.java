package com.mycompany.leetcode.blind75.tree.SerializeAndDeserializeBinaryTree;

import com.mycompany.leetcode.blind75.tree.Tree;
import com.mycompany.leetcode.blind75.tree.TreeNode;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SerializeAndDeserializeBinaryTreeGavinlinasd {
    private static final String spliter = ",";
    private static final String NN = "X";

    // Encodes a tree to a single string.
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

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(spliter)));
        return buildTree(nodes);
    }

    private TreeNode buildTree(Deque<String> nodes) {
        String val = nodes.remove();
        if (val.equals(NN)) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(nodes);
            node.right = buildTree(nodes);
            return node;
        }
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3, new  TreeNode(4), new TreeNode(5)));

        new Tree().printPostorder(root);
        System.out.println();
        SerializeAndDeserializeBinaryTreeGavinlinasd obj = new SerializeAndDeserializeBinaryTreeGavinlinasd();
        String result = obj.serialize(root);
        System.out.println(result);

        TreeNode treeNode = obj.deserialize(result);

        new Tree().printPostorder(treeNode);


    }
}
