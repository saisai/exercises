package com.mycompany.leetcode.blind75.DynamicProgramming.HouseRobber;

import java.util.Arrays;

public class HouseRobberHeroes3001 {
    static int iterativeMemoBottomUpRob(int[] nums) {
        if(nums.length == 0) return 0;
        int[] memo = new int[nums.length + 1];
        memo[0] = 0;
        memo[1] = nums[0];
        for(int i = 1; i < nums.length; i++) {
            int val = nums[i];
            memo[i+1] = Math.max(memo[i], memo[i-1] + val);
        }
        return memo[nums.length];
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,1};
        System.out.println(Arrays.toString(new int[]{iterativeMemoBottomUpRob(nums)}));
    }
}
