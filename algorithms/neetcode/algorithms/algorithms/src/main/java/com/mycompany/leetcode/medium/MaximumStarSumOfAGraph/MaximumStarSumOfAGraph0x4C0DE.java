package com.mycompany.leetcode.medium.MaximumStarSumOfAGraph;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class MaximumStarSumOfAGraph0x4C0DE {
    static int maxStarSum(int[] vals, int[][] edges, int k) {
        Map<Integer, Queue<Integer>> graph = new HashMap<>();
        for(int[] edge : edges) {

            graph.putIfAbsent(edge[0], new PriorityQueue<>());
            if(vals[edge[1]] > 0) {
                Queue<Integer> queue = graph.get(edge[0]);
                queue.offer(vals[edge[1]]);
                if(queue.size() > k) {
                    queue.poll();
                }
            }

            graph.putIfAbsent(edge[1], new PriorityQueue<>());
            if(vals[edge[0]] > 0) {
                Queue<Integer> queue = graph.get(edge[1]);
                queue.offer(vals[edge[0]]);
                if(queue.size() > k) {
                    queue.poll();
                }
            }
        }

        int result = Integer.MIN_VALUE;
        for(int star : vals) {
            result = Math.max(result, star);
        }

        for(Map.Entry<Integer, Queue<Integer>> entry : graph.entrySet()) {
            int sum = vals[entry.getKey()];
            for(int star : entry.getValue()) {
                sum += star;
            }

            result = Math.max(result, sum);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] vals = {1,2,3,4,10,-10,-20};
        int[][] edges = {{0,1},{1,2},{1,3},{3,4},{3,5},{3,6}};
        int k = 2;

        System.out.println(maxStarSum(vals, edges, k));
    }
}
