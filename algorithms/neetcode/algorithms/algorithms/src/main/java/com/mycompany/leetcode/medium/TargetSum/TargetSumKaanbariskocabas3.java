package com.mycompany.leetcode.medium.TargetSum;

import java.util.HashMap;
import java.util.Map;

public class TargetSumKaanbariskocabas3 {
    static int dp(int i, int sum, int[] nums, Map<String, Integer> memo) {
        if(i == nums.length) {
            return sum == 0 ? 1 : 0;
        }
        String key = new StringBuilder().append(i).append(",").append(sum).toString();
        if(!memo.containsKey(key)) {
            int add = dp(i + 1, sum + nums[i], nums, memo);
            int substract = dp(i + 1, sum - nums[i], nums, memo);
            memo.put(key, add + substract);
        }

        return memo.get(key);
    }

    static int findTargetSumWays(int[] nums, int target) {
        Map<String, Integer> memo = new HashMap<>();
        return dp(0, -target, nums, memo);
    }

    public static void main(String[] args) {
        int[] nums ={1,1,1,1,1};
        int target = 3;
        int[] nums2 ={1,1,1};
        int target2 = 1;
        //System.out.println(findTargetSumWays(nums, target));
        System.out.println(findTargetSumWays(nums2, target2));
    }
}
