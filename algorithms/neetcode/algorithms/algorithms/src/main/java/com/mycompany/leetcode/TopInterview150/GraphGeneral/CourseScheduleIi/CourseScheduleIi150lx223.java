package com.mycompany.leetcode.TopInterview150.GraphGeneral.CourseScheduleIi;

import java.util.*;

public class CourseScheduleIi150lx223 {
    private void initialiseGraph(int[] incLinkCounts, List<List<Integer>> adjs, int[][] prerequisites) {
        int n = incLinkCounts.length;
        while(n-- > 0) adjs.add(new ArrayList<>());
        for(int[] edge : prerequisites) {
            incLinkCounts[edge[0]]++;
            adjs.get(edge[1]).add(edge[0]);
        }
    }

    private int[] solveByBFS(int[] incLinkCounts, List<List<Integer>> adjs) {
        int[] order = new int[incLinkCounts.length];
        Queue<Integer> toVisit = new ArrayDeque<>();
        for(int i = 0; i < incLinkCounts.length; i++) {
            if(incLinkCounts[i] == 0) toVisit.offer(i);
        }
        int visited = 0;

        while(!toVisit.isEmpty()) {
            int from = toVisit.poll();
            order[visited++] = from;
            for(int to : adjs.get(from)) {
                incLinkCounts[to]--;
                if(incLinkCounts[to] == 0) toVisit.offer(to);
            }
        }

        return visited == incLinkCounts.length ? order : new int[0];
    }

    private int[] solveByDFS(List<List<Integer>> adjs) {
        BitSet hasCycle = new BitSet(1);
        BitSet visited = new BitSet(adjs.size());
        BitSet onStack = new BitSet(adjs.size());
        Deque<Integer> order = new ArrayDeque<>();
        for (int i = adjs.size() - 1; i >= 0; i--) {
            if (visited.get(i) == false && hasOrder(i, adjs, visited, onStack, order) == false) return new int[0];
        }
        int[] orderArray = new int[adjs.size()];
        for (int i = 0; !order.isEmpty(); i++) orderArray[i] = order.pop();
        return orderArray;
    }

    private boolean hasOrder(int from, List<List<Integer>> adjs, BitSet visited, BitSet onStack, Deque<Integer> order) {
        visited.set(from);
        onStack.set(from);
        for (int to : adjs.get(from)) {
            if (visited.get(to) == false) {
                if (hasOrder(to, adjs, visited, onStack, order) == false) return false;
            } else if (onStack.get(to) == true) {
                return false;
            }
        }
        onStack.clear(from);
        order.push(from);
        return true;
    }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] incLinkCounts = new int[numCourses];
        List<List<Integer>> adjs = new ArrayList<>(numCourses);
        initialiseGraph(incLinkCounts, adjs, prerequisites);
        //return solveByBFS(incLinkCounts, adjs);
        return solveByDFS(adjs);
    }

    public static void main(String[] args) {
        int numCourses = 4;
        int[][] prerequisites = {{1,0},{2,0},{3,1},{3,2}};
        CourseScheduleIi150lx223 obj = new CourseScheduleIi150lx223();
        int[] results = obj.findOrder(numCourses, prerequisites);
        System.out.println(Arrays.toString(results));
    }
}
