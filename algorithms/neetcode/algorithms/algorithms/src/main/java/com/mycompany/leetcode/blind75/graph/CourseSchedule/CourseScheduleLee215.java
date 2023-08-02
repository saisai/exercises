package com.mycompany.leetcode.blind75.graph.CourseSchedule;

import java.util.ArrayList;

public class CourseScheduleLee215 {
    static boolean canFinish(int n, int[][] prerequisites) {
        ArrayList<Integer>[] G = new ArrayList[n];
        int[] degree = new int[n];
        ArrayList<Integer> bfs = new ArrayList<>();
        for(int i = 0; i < n; i++) G[i] = new ArrayList<Integer>();
        for(int[] e : prerequisites) {
            G[e[1]].add(e[0]);
            degree[e[0]]++;
        }
        for(int i = 0; i < n; ++i) if(degree[i] == 0) bfs.add(i);
        for(int i = 0; i <bfs.size(); ++i) {
            for(int j : G[bfs.get(i)]) {
                if(--degree[j] == 0) bfs.add(j);
            }
        }
        return bfs.size() == n;
    }

    public static void main(String[] args) {
        int numCourses = 2;
        int[][] prerequisites = {{1,0}};
        System.out.println(canFinish(numCourses, prerequisites));
    }
}
