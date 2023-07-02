package com.mycompany.leetcode.medium.TargetSum;

import java.util.HashMap;
import java.util.Map;

public class TargetSumAnarchaworld {
    static int findTargetSumWays(int[] nums, int target) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 1);
        for(int n : nums) {
            Map<Integer, Integer> ndp = new HashMap<>();
            for(int key : dp.keySet()) {
                ndp.merge(key - n, dp.get(key), Integer::sum);
                ndp.merge(key + n, dp.get(key), Integer::sum);
            }
            dp = ndp;
        }
        return dp.getOrDefault(target, 0);
    }

    public static void main(String[] args) {
        int[] nums ={1,1,1,1,1};
        int target = 3;
        System.out.println(findTargetSumWays(nums, target));
    }
}
