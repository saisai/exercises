package com.mycompany.leetcode.medium.FindTheScoreOfAllPrefixesOfAnArray;

import java.util.Arrays;

public class FindTheScoreOfAllPrefixesOfAnArrayRock {
    static long[] findPrefixScore(int[] nums) {
        int n = nums.length;
        long[] score = new long[n + 1];
        for(int i = 0, max = 0; i < n; ++i) {
            max = Math.max(max, nums[i]);
            score[i + 1] += score[i] + max + nums[i];
        }
        return Arrays.copyOfRange(score, 1, n + 1);
    }

    public static void main(String[] args) {
        int[] nums = {2,3,7,5,10};
        long[] result = findPrefixScore(nums);
        System.out.println(Arrays.toString(result));
    }
}
