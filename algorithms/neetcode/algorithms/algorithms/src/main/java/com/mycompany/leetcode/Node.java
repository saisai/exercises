package com.mycompany.leetcode;

public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }

    public void printInorder(Node node) {
        if(node == null)
            return;

        // first recur on left child
        printInorder(node.left);

        System.out.printf("%d ", node.val);

        // recur on right child

        printInorder(node.right);


    }

    public void printPreorder(Node node) {
        if(node == null)
            return;

        System.out.printf("%d ", node.val);

        // first recur on left child
        printInorder(node.left);



        // recur on right child

        printInorder(node.right);


    }


    public void printPostorder(Node node) {
        if(node == null)
            return;



        // first recur on left child
        printInorder(node.left);



        // recur on right child

        printInorder(node.right);

        System.out.printf("%d ", node.val);

    }

    int height(Node root)
    {
        if (root == null)
            return 0;
        else {
            /* compute  height of each subtree */
            int lheight = height(root.left);
            int rheight = height(root.right);

            /* use the larger one */
            if (lheight > rheight)
                return (lheight + 1);
            else
                return (rheight + 1);
        }
    }

    void printCurrentLevel(Node root, int level)
    {
        if (root == null)
            return;
        if (level == 1)
            System.out.print(root.val + " ");
        else if (level > 1) {
            printCurrentLevel(root.left, level - 1);
            printCurrentLevel(root.right, level - 1);
        }
    }

    public void printLevelOrder(Node root)
    {
        int h = height(root);
        int i;
        for (i = 1; i <= h; i++)
            printCurrentLevel(root, i);
    }

};
