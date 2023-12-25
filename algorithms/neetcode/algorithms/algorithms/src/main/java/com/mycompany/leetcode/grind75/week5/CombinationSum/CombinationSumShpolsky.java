package com.mycompany.leetcode.grind75.week5.CombinationSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombinationSumShpolsky {
   public List<List<Integer>> combinationSums(int[] cands, int t) {
        Arrays.sort(cands); // sort candidates to try them in asc order
        List<List<List<Integer>>> dp = new ArrayList<>();
        for (int i = 1; i <= t; i++) { // run through all targets from 1 to t
            List<List<Integer>> newList = new ArrayList(); // combs for curr i
            // run through all candidates <= i
            for (int j = 0; j < cands.length && cands[j] <= i; j++) {
                // special case when curr target is equal to curr candidate
                if (i == cands[j]) newList.add(Arrays.asList(cands[j]));
                    // if current candidate is less than the target use prev results
                else {
                    for (List<Integer> l : dp.get(i - cands[j] - 1)) {
                        if (cands[j] <= l.get(0)) {
                            List cl = new ArrayList<>();
                            cl.add(cands[j]);
                            cl.addAll(l);
                            newList.add(cl);
                        }
                    }
                }
            }
            dp.add(newList);
        }
        return dp.get(t-1);
    }

    public static void main(String[] args) {
        int[] candidates = {2,6,3,7};
        int target = 7;

        CombinationSumShpolsky obj = new CombinationSumShpolsky();
        System.out.println(obj.combinationSums(candidates, target));

    }
}
