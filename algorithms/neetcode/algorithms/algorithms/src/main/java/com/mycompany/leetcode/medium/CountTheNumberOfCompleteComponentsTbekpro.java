package com.mycompany.leetcode.medium;

import java.util.*;

public class CountTheNumberOfCompleteComponentsTbekpro {

    private static void dfs(int i, Map<Integer, List<Integer>> map,
                            Set<Integer> visited, Set<Integer> visitedNow) {
        if(visited.contains(i)) return;

        visited.add(i);
        visitedNow.add(i);
        List<Integer> list = map.get(i);
        if(list != null) {
            for(int j = 0; j < list.size(); j++) {
                dfs(list.get(j), map, visited, visitedNow);
            }
        }
    }

    private static int countCompleteComponents(int n, int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int[] conn : edges) {
            int one = conn[0], two = conn[1];
            if(!map.containsKey(one)) map.put(one, new ArrayList<>());
            map.get(one).add(two);
            if(!map.containsKey(two)) map.put(two, new ArrayList<>());
            map.get(two).add(one);
        }

        Set<Integer> visited = new HashSet<>(), visitedNow = new HashSet<>();
        int res = 0;
        for(int i = 0; i < n; i++) {
            dfs(i, map, visited, visitedNow);
            boolean isComponent = false;
            for(int vis : visitedNow) {
                isComponent = true;
                if(map.containsKey(vis) && map.get(vis).size() != visitedNow.size() - 1) {
                    isComponent = false;
                    break;
                }
            }

            if(isComponent) res++;
            visitedNow = new HashSet<>();
        }
        return  res;
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] edges = {{0,1},{0,2},{1,2},{3,4}};
        int result = countCompleteComponents(n, edges);
        System.out.println(result);
    }

}
