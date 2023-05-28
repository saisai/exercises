package com.mycompany.leetcode.hard.SimilarStringGroups;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SimilarStringGroupAkash0228GraphSolution {
    static boolean isSimilar(String s1, String s2) {
        int diff = 0;
        for(int i = 0; i < s1.length(); i++) {
            if(s1.charAt(i) != s2.charAt(i))
                diff++;
        }
        return diff == 0 || diff == 2;
    }

    static void dfs(int curr, HashMap<Integer, List<Integer>> graph, boolean[] visited) {
        visited[curr] = true;
        if(!graph.containsKey(curr))
            return;
        List<Integer> neigh = graph.get(curr);
        for(int node : neigh) {
            if(!visited[node]) {
                dfs(node, graph, visited);
            }
        }
    }

    static int numSimiliarGroups(String[] strs) {
        int n = strs.length;
        HashMap<Integer, List<Integer>> map = new HashMap<>();

        // creating graph
        for(int i=0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                if(isSimilar(strs[i], strs[j])) {
                    if(map.containsKey(i)) {
                        map.get(i).add(j);
                    } else {
                        map.put(i, new ArrayList<>());
                        map.get(i).add(j);
                    }

                    if(map.containsKey(j)) {
                        map.get(j).add(i);
                    } else {
                        map.put(j, new ArrayList<>());
                        map.get(j).add(i);
                    }
                }
            }
        }

        boolean[] visited = new boolean[n];
        int count = 0;

        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                count++;
                dfs(i, map,visited);
            }
        }

        return count;
    }

    public static void main(String[] args) {
        String[] strs = {"tars","rats","arts","star"};
        System.out.println(numSimiliarGroups(strs));
    }
}
