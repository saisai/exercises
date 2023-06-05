package com.mycompany.leetcode.hard.NumberOfWaysToStayInTheSamePlaceAfterSomeSteps;

public class NumberOfWaysToStayInTheSamePlaceAfterSomeStepsChappy1 {

    static int numWays(int steps, int arrLen) {
        int mod = (int)1e9+7, maxpos = Math.min(steps/2+1, arrLen);
        int[] dp = new int[maxpos];
        dp[0] = 1;
        for(int i = 1; i <= steps; ++i) {
            int[] next = new int[maxpos];
            for(int j=0; j < maxpos; ++j) {
                next[j] = dp[j];
                if(j > 0) next[j] = (next[j] + dp[j-1]) % mod;
                if(j < maxpos - 1) next[j] = (next[j] + dp[j+1]) % mod;
            }
            dp = next;
        }
        return (int)dp[0];
    }

    public static void main(String[] args) {
        int steps = 3, arrLen = 2;
        System.out.println(numWays(steps, arrLen));
    }
}
