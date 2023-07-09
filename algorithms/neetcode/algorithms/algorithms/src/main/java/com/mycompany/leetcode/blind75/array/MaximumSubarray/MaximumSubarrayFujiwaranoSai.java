package com.mycompany.leetcode.blind75.array.MaximumSubarray;

public class MaximumSubarrayFujiwaranoSai {
    public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];
        dp[0] = A[0];
        int max = dp[0];

        for(int i= 1; i < n; i++) {
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }

        return max;
    }

    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        MaximumSubarrayFujiwaranoSai obj = new MaximumSubarrayFujiwaranoSai();
        System.out.println(obj.maxSubArray(nums));
    }
}
