package com.mycompany.leetcode.blind75.DynamicProgramming.LongestIncreasingSubsequence;

public class LongestIncreasingSubsequenceDietpepsi {
    static int lenghtOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for(int x : nums) {
            int i = 0, j = size;
            while(i != j) {
                int m = (i + j) / 2;
                if(tails[m] < x)
                    i = m + 1;
                else
                    j = m;

            }
            tails[i] = x;
            if(i == size) ++size;
        }
        return size;
    }

    public static void main(String[] args) {
        int[] nums = {10,9,2,5,3,7,101,18};
        System.out.println(lenghtOfLIS(nums));
    }
}
