package com.mycompany.leetcode.randomly.dfs;

import java.util.*;

public class RedundantConnectionNaveenKothamasu {
    private boolean dfs(int u, int v, int pre, List<Set<Integer>> adjList) {
        if(u == v)
            return true;
        for(int w : adjList.get(u)) {
            if(w == pre) continue;
            boolean ret = dfs(w, v, u, adjList);
            if(ret) return true;
        }
        return false;
    }

    public int[] findRedundantConnection(int[][] edges) {
        int[] ret = null;
        int n = edges.length;
        List<Set<Integer>> adjList = new ArrayList<>(1001);
        for(int i = 0; i < 1001; i++) {
            adjList.add(new HashSet<>());
        }

        for(int[] edge : edges) {
            int u = edge[0], v = edge[1];
            if(dfs(u, v, 0, adjList)) {
                ret = edge;
            }else {
                adjList.get(u).add(v);
                adjList.get(v).add(u);
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        int[][] edges = {{1,2},{1,3},{2,3}};

        RedundantConnectionNaveenKothamasu obj = new RedundantConnectionNaveenKothamasu();
        int[] result = obj.findRedundantConnection(edges);
        System.out.println(Arrays.stream(result).spliterator());
        System.out.println(Arrays.toString(result));
    }
}


 // https://stackoverflow.com/questions/409784/whats-the-simplest-way-to-print-a-java-array
// https://leetcode.com/u/naveen_kothamasu/
// https://leetcode.com/problems/redundant-connection/solutions/277026/dfs-java-solution-with-explanation/