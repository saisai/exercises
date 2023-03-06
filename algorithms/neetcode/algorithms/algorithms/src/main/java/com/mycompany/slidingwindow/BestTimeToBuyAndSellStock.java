package com.mycompany.slidingwindow;

public class BestTimeToBuyAndSellStock {

    public int maxProfit2(int[] prices) {
        int oldStockPrice = prices[0];
        int profit = 0;
        for(int i = 1; i<prices.length; i++){
            if(prices[i]<oldStockPrice){
                oldStockPrice = prices[i];
            }else{
                profit+=prices[i]-oldStockPrice;
                oldStockPrice = prices[i];
            }
        }
        return profit;
    }

    // not working there is bug need to fix.
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProfitResult = 0;
        while( left < prices.length) {
            if(prices[left] < prices[right]) {
                maxProfitResult = Math.max(maxProfitResult, prices[right] - prices[left]);
                right++;
            } else {
                left = right;
                right++;
            }
        }
        System.out.println(maxProfitResult);
        return maxProfitResult;
    }
    public static void main(String[] args) {
        BestTimeToBuyAndSellStock s = new BestTimeToBuyAndSellStock();
        int[] prices = {7,1,5,3,6,4};

        System.out.println(s.maxProfit2(prices));
    }
}
