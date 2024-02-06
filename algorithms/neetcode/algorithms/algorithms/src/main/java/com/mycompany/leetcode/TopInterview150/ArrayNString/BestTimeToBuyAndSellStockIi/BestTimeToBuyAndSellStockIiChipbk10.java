package com.mycompany.leetcode.TopInterview150.ArrayNString.BestTimeToBuyAndSellStockIi;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BestTimeToBuyAndSellStockIiChipbk10 {
    public int maxProfit(int[] prices) {
        int i = 0, buy, sell, profit =0, N = prices.length - 1;
        while(i < N) {
            while(i < N && prices[i + 1] <= prices[i]) i++;
            buy = prices[i];

            while(i < N && prices[i + 1] > prices[i]) i++;
            sell = prices[i];

            profit += sell - buy;
        }
        return profit;
    }

    public Pair<List<Pair<Integer, Integer>>, Integer> buysAndSells(int[] prices) {
        int i = 0, iBuy, iSell, profit = 0, N = prices.length - 1;
        List<Pair<Integer, Integer>> buysAndSells = new ArrayList<Pair<Integer, Integer>>();
        while(i < N) {
            while(i < N && prices[i + 1] <= prices[i]) i++;
            iBuy = i;

            while(i < N && prices[i + 1] > prices[i]) i++;
            iSell = i;

            profit += prices[iSell] - prices[iBuy];
            Pair<Integer, Integer> bs = new Pair<Integer, Integer>(iBuy, iSell);
            buysAndSells.add(bs);
        }
        return new Pair<List<Pair<Integer, Integer>>, Integer>(buysAndSells, profit);
    }

    static class Pair<T1, T2> {
        private T1 fst;
        private T2 snd;
        public Pair(T1 f, T2 s) {
            fst = f;
            snd = s;
        }
    }

    public static void main(String[] args) {
        BestTimeToBuyAndSellStockIiChipbk10 obj = new BestTimeToBuyAndSellStockIiChipbk10();
        int[] prices = {7,1,5,3,6,4};
//        System.out.println(obj.maxProfit(prices));
        Pair<List<Pair<Integer, Integer>>, Integer> result = obj.buysAndSells(prices);

        System.out.println(" test " + result.snd);
        result.fst.forEach(lst -> {
            System.out.println(lst.fst + " " + lst.snd);
        });
    }
}
