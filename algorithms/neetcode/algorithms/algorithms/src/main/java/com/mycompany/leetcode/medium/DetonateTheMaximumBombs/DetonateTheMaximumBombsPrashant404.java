package com.mycompany.leetcode.medium.DetonateTheMaximumBombs;

import java.lang.reflect.MalformedParameterizedTypeException;
import java.util.*;

public class DetonateTheMaximumBombsPrashant404 {

    private static Map<Integer, List<Integer>> getAdjacencyList2(int n, int[][] bombs) {
        Map<Integer, List<Integer>> graph = new HashMap<Integer, List<Integer>>();

        for(int i = 0; i < n; i++)
            graph.put(i, new ArrayList<>());

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++) {
                double distance = Math.hypot(bombs[i][0] - bombs[j][0], bombs[i][1] - bombs[j][i]);

                if(distance <= bombs[i][2])
                    graph.get(i).add(j);
                if(distance <= bombs[j][2])
                    graph.get(j).add(i);
            }
        }
        return graph;
    }

    private static Map<Integer, List<Integer>> getAdjacencyList(int n, int[][] bombs) {
        var graph = new HashMap<Integer, List<Integer>>();

        for (var i = 0; i < n; i++)
            graph.put(i, new ArrayList<>());

        for (var i = 0; i < n; i++)
            for (var j = i + 1; j < n; j++) {
                var distance = Math.hypot(bombs[i][0] - bombs[j][0], bombs[i][1] - bombs[j][1]);

                if (distance <= bombs[i][2])
                    graph.get(i).add(j);
                if (distance <= bombs[j][2])
                    graph.get(j).add(i);
            }

        return graph;
    }

    public static int maximumDetonation(int[][] bombs) {
        int n = bombs.length;
        Map<Integer, List<Integer>> graph = getAdjacencyList(n, bombs);
        System.out.println(graph);
        int maxBombs = 1;

        for(int i = 0; i < n; i++) {
            Set<Integer> visited = new HashSet<>(List.of(i));

            for(var q = new ArrayDeque<>(List.of(i)); !q.isEmpty();) {
                for(var next : graph.get(q.poll()))
                    if(visited.add(next))
                        q.add(next);

            }
            maxBombs = Math.max(maxBombs, visited.size());
        }

        return maxBombs;
    }

    public static void main(String[] args) {
        int[][] bombs = {{2,1,3},{6,1,4}};
        System.out.println(maximumDetonation(bombs));
    }
}
