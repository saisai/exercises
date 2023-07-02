package com.mycompany.leetcode.medium.MaximumStarSumOfAGraph;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MaximumStarSumOfAGraphYe15 {
    static int maxStarSum(int[] vals, int[][] edges, int k) {
        int n = vals.length;
        List<Integer>[] graph = new ArrayList[n];
        for(int u = 0; u < n; ++u) graph[u] = new ArrayList<>();
        for(int[] e: edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        int ans = Integer.MIN_VALUE;
        for(int u = 0; u < n; ++u) {
            int cand = vals[u];
            if(graph[u].size() > k) Collections.sort(graph[u], (a, b) -> vals[b] - vals[a]);
            for(int v = 0; v < k && v < graph[u].size(); ++v)
                cand += Math.max(0, vals[graph[u].get(v)]);

            ans = Math.max(ans, cand);
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] vals = {1,2,3,4,10,-10,-20};
        int[][] edges = {{0,1},{1,2},{1,3},{3,4},{3,5},{3,6}};
        int k = 2;

        System.out.println(maxStarSum(vals, edges, k));
    }
}
