package com.mycompany.leetcode.TopInterview150.ArrayNString.BestTimeToBuyAndSellStock;

public class BestTimeToBuyAndSellStockHimalik {
    public int maxProfit(int[] prices) {
        int lst = Integer.MAX_VALUE;
        int op = 0;
        int pist = 0;

        for(int i = 0; i < prices.length; i++) {
            if(prices[i] < lst) {
                lst = prices[i];
            }
            pist = prices[i] - lst;
            if(op < pist) {
                op = pist;
            }
        }
        return op;
    }

    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        BestTimeToBuyAndSellStockHimalik obj = new BestTimeToBuyAndSellStockHimalik();
        System.out.println(obj.maxProfit(prices));
    }
}
