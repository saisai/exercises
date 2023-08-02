package com.mycompany.leetcode.blind75.graph.CloneGraph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CloneGraphAkshatsankhyan {
    static class Node {
        public int val;
        public List<Node> neighbors;
        public Node() {
            val = 0;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }

    static void dfs(Node node, Node copy, Node[] visited) {
        visited[copy.val] = copy;

        for(Node n : node.neighbors) {
            if(visited[n.val] == null) {
                Node newNode=  new Node(n.val);
                copy.neighbors.add(newNode);
                dfs(n, newNode, visited);
            } else {
                copy.neighbors.add(visited[n.val]);
            }
        }
    }

    static Node cloneGraph(Node node) {
        if(node == null) return null;
        Node copy = new Node(node.val);
        Node[] visited = new Node[101];
        Arrays.fill(visited, null);
        dfs(node, copy, visited);
        return copy;
    }

    public static void main(String[] args) {
        int[][] adjList = {{2,4},{1,3},{2,4},{1,3}};
        Node result = new Node();
        //result = cloneGraph(adjList);
    }
}
