package com.mycompany.leetcode.grind75.week3.KClosestPointsToOrigin;

import java.util.Arrays;
import java.util.PriorityQueue;

public class KClosestPointsToOriginFrimish {
    public int[][] kCloset(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);
        for(int[] p : points) {
            pq.offer(p);
            if(pq.size() > k) {
                pq.poll();
            }
        }
        int[][] res = new int[k][2];
        while(k > 0) {
            res[--k] = pq.poll();
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] points = {{1,3},{-2,2}};
        int k = 1;
        KClosestPointsToOriginFrimish obj = new KClosestPointsToOriginFrimish();
        System.out.println(Arrays.deepToString(obj.kCloset(points, k)));
    }
}
