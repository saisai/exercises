package com.mycompany.leetcode.medium;

import java.util.Arrays;

public class SumInAMatrixTbekpro2 {
    private static void makeReverse(int[] num) {
        for(int i = 0; i < num.length / 2; i++) {
            int temp = num[i];
            num[i] = num[num.length - 1 - i];
            num[num.length - 1 - i] = temp;
        }
    }

    private static int matrixSum(int[][] nums) {
        for(int i = 0; i < nums.length; i++) {
            Arrays.sort(nums[i]);
            //makeReverse(nums[i]);
        }

        int max = 0, sum = 0;
        for(int i = 0; i < nums[0].length; i++) {
            for(int j = 0 ; j < nums.length; j++) if(max < nums[j][i]) max = nums[j][i];
            sum += max;
            max = 0;
        }
        return sum;
    }

    public static void main(String[] args) {
        int[][] nums = {{7,2,1},{6,4,2},{6,5,3},{3,2,1}};
        System.out.println(matrixSum(nums));
    }

}
