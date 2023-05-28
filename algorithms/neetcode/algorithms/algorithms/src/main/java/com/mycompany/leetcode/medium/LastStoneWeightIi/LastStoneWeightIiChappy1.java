package com.mycompany.leetcode.medium.LastStoneWeightIi;

public class LastStoneWeightIiChappy1 {
    static int lastStoneWeightII(int[] A) {
        boolean[] dp = new boolean[1501];
        dp[0] = true;
        int sumA = 0;
        for(int a : A) {
            sumA += a;
            for(int i = Math.min(1500, sumA); i >= a; --i)
                dp[i] |= dp[i-a];
        }
        for(int i = sumA / 2; i >= 0; --i)
            if(dp[i]) return sumA - i - i;
        return 0;
    }

    public static void main(String[] args) {
        int[] stones = {2,7,4,1,8,1};
        System.out.println(lastStoneWeightII(stones));
    }
}
