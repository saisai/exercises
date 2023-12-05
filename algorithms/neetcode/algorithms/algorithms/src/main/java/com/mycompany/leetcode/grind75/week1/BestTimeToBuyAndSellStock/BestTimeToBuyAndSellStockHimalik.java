package com.mycompany.leetcode.grind75.week1.BestTimeToBuyAndSellStock;

public class BestTimeToBuyAndSellStockHimalik {
    public int maxProfit(int[] prices) {
        int lsf = Integer.MAX_VALUE;
        int op = 0;
        int pist = 0;

        for(int i = 0; i < prices.length; i++) {
            if(prices[i] < lsf) {
                lsf = prices[i];
            }
            pist  = prices[i] - lsf;
            if(op < pist) {
                op = pist;
            }
        }
        return op;
    }

    public static void main(String[] args) {

        int[][] prices = { {7,1,5,3,6,4},
                {7,6,4,3,1} };
        BestTimeToBuyAndSellStockHimalik obj = new BestTimeToBuyAndSellStockHimalik();
        for(int[] price : prices) {
            System.out.println(obj.maxProfit(price));
        }

    }
}
