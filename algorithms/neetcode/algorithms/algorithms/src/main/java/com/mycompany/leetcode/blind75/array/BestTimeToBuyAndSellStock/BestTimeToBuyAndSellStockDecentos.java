package com.mycompany.leetcode.blind75.array.BestTimeToBuyAndSellStock;

public class BestTimeToBuyAndSellStockDecentos {
    public int maxProfit(int[] prices) {
        int minBuy = prices[0], maxProfit = 0;
        for(int current : prices) {
            minBuy = Math.min(minBuy, current);
            maxProfit = Math.max(maxProfit, current - minBuy);
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        BestTimeToBuyAndSellStockDecentos obj = new BestTimeToBuyAndSellStockDecentos();
        int[] prices = {7,1,5,3,6,4};
        System.out.println(obj.maxProfit(prices));
    }
}

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/2795048/java-runtime-1ms-faster-than-100-o-n-time-o-1-space/
