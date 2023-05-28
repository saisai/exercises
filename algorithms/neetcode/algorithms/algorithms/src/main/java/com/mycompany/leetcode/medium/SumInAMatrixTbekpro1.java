package com.mycompany.leetcode.medium;

import java.util.Comparator;
import java.util.PriorityQueue;

public class SumInAMatrixTbekpro1 {

    private static int matrixSum(int[][] nums) {
        PriorityQueue<Integer> arr[] = new PriorityQueue[nums.length];
        for(int i = 0; i < nums.length; i++) {
            arr[i] = new PriorityQueue<>(Comparator.reverseOrder());
            for(int j = 0 ;j < nums[i].length; j++) arr[i].offer(nums[i][j]);
        }

        int localMax = 0, sum = 0;
        while(!arr[0].isEmpty()) {
            for(int i = 0; i < arr.length; i++) {
                int curr = arr[i].poll();
                if(localMax < curr) localMax = curr;
            }
            sum += localMax;
            localMax = 0;
        }
        return  sum;
    }

    public static void main(String[] args) {
        int[][] nums = {{7,2,1},{6,4,2},{6,5,3},{3,2,1}};
        System.out.println(matrixSum(nums));
    }

}
