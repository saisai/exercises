package com.mycompany.leetcode.blind75.DynamicProgramming.UniquePaths;

import java.util.Arrays;

public class UniquePathsFLlGHT {
    static int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for(int i = 1; i < m; i++) {
            for(int j = 1;  j <n; j++)
                dp[i] += dp[j - 1];
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        int m = 3, n = 7;
        System.out.print(uniquePaths(m, n));
    }
}
