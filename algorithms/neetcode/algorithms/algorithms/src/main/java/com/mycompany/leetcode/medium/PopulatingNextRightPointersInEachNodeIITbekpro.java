package com.mycompany.leetcode.medium;

import com.mycompany.leetcode.Node;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PopulatingNextRightPointersInEachNodeIITbekpro {

    private static void goDFS(Node node, int lvl, Map<Integer, List<Node>> map) {
        if(node == null) return;

        List<Node> list = map.computeIfAbsent(lvl, ArrayList::new);
        list.add(node);
        lvl++;
        goDFS(node.left, lvl, map);
        goDFS(node.right, lvl, map);
    }

    private static Node connect(Node root) {
        Map<Integer, List<Node>> map = new HashMap<>();
        goDFS(root, 0, map);
        for(List<Node> list : map.values()) {
            for(int i = 1; i < list.size(); i++) {
                list.get(i - 1).next = list.get(i);
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right = new Node(3);
        root.right.right = new Node(4);

        Node result = connect(root);

        root.printInorder(result);
        System.out.println();
        root.printPreorder(result);
        System.out.println();

        root.printPostorder(result);
        System.out.println();

        root.printLevelOrder(result);
    }
}


// https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
// https://www.geeksforgeeks.org/level-order-tree-traversal/