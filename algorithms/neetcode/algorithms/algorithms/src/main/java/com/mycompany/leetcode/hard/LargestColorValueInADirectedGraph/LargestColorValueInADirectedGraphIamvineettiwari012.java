package com.mycompany.leetcode.hard.LargestColorValueInADirectedGraph;

import java.util.ArrayList;
import java.util.List;

public class LargestColorValueInADirectedGraphIamvineettiwari012 {
    List<List<Integer>> graph;
    boolean visited[];
    int counts[][];


    private int countInPath(int node, boolean pathVisited[], String colors) {
        if(pathVisited[node]) {
            return Integer.MAX_VALUE;
        }

        int idx = colors.charAt(node) - 'a';

        if(visited[node]) {
            return counts[node][idx];
        }

        visited[node] = true;
        pathVisited[node] = true;

        for(int adj : graph.get(node)) {
            int data = countInPath(adj, pathVisited, colors);

            if(data == Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }

            for(int i = 0; i < 26; i++) {
                counts[node][i] = Math.max(counts[node][i], counts[adj][i]);
            }
        }

        counts[node][idx]++;
        pathVisited[node] = false;

        return counts[node][idx];
    }

    public int largestPathValue(String colors, int[][] edges) {
        int max = -1;
        int nodes = colors.length();
        counts = new int[nodes][26];
        visited = new boolean[nodes];

        graph = new ArrayList<>();

        for(int i = 0; i < nodes; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] edge: edges) {
            int source = edge[0];
            int dest = edge[1];

            graph.get(source).add(dest);
        }

        for(int i = 0; i < nodes; i++) {
            boolean pathVisited[] = new boolean[nodes];
            int count = countInPath(i, pathVisited, colors);
            max = Math.max(count, max);
        }

        return max == Integer.MIN_VALUE ? -1 : max;
    }

    public static void main(String[] args) {
        String colors = "abaca";
        int[][] edges = {{0,1},{0,2},{2,3},{3,4}};

        LargestColorValueInADirectedGraphIamvineettiwari012 obj = new LargestColorValueInADirectedGraphIamvineettiwari012();

        System.out.println(obj.largestPathValue(colors, edges));
    }
}
