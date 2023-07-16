package com.mycompany.leetcode.blind75.DynamicProgramming.CoinChange;

public class CoinChangeYu6 {
    static int coinChange(int[] coins, int amount) {
        if(amount < 0) return -1;
        if(amount == 0) return 0;
        int cc = -1;
        for(int i = 0; i < coins.length; i++) {
            int coin = coinChange(coins, amount-coins[i]);
            if(coin >= 0) cc = cc < 0 ? coin + 1 : Math.min(cc, coin + 1);
        }
        return cc;
    }

    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.println(coinChange(coins, amount));
    }
}
