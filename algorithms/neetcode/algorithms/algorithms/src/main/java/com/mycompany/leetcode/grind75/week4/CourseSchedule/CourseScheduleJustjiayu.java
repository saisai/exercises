package com.mycompany.leetcode.grind75.week4.CourseSchedule;

import java.util.*;

public class CourseScheduleJustjiayu {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] indegree = new int[numCourses];

        for(int i = 0; i < prerequisites.length; i++) {
            int ready = prerequisites[i][0];
            int pre = prerequisites[i][1];
            if(matrix[pre][ready] == 0) {
                indegree[ready]++;
            }
            matrix[pre][ready] = 1;
        }

        int count = 0;
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < indegree.length; i++) {
            if(indegree[i] == 0) queue.offer(i);
        }

        while(!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for(int i=0; i < numCourses; i++) {
                if(matrix[course][i] != 0) {
                    if(--indegree[i] == 0) {
                        queue.offer(i);
                    }
                }
            }
        }

        return count == numCourses;
    }

    public static void main(String[] args) {
        CourseScheduleJustjiayu obj = new CourseScheduleJustjiayu();
        int numCourses = 2;
        int[][] prerequisites = {{1,0}};

        //System.out.println(obj.canFinish(numCourses, prerequisites));
//        Map<Integer, int[][]> map = new HashMap<Integer, int[][]>(){{
//            put(2, new int[][] {{1, 0}});
//        }};
//
//        for(Map.Entry<Integer, int[][]> entry : map.entrySet()) {
//            System.out.println(entry.getKey());
//            System.out.println(Arrays.deepToString(entry.getValue()));
//            System.out.println(obj.canFinish(entry.getKey(), entry.getValue()));
//        }

        Map<Integer, int[][]> map = new HashMap<Integer, int[][]>();
        map.put(2, new int[][] {{1, 0}});
        //map.put(2, new int[][] {{1, 0}, {0, 1}});

        for(Map.Entry<Integer, int[][]> entry : map.entrySet()) {
            System.out.println(entry.getKey());
            System.out.println(Arrays.deepToString(entry.getValue()));
            System.out.println(obj.canFinish(entry.getKey(), entry.getValue()));
        }



    }
}
