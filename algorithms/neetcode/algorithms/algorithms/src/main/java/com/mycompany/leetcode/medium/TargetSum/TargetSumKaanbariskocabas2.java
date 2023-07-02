package com.mycompany.leetcode.medium.TargetSum;

public class TargetSumKaanbariskocabas2 {
    static int ans = 0;

    static void backtrack(int i, int sum, int[] nums) {
        if(i == nums.length) {
            if(sum == 0) ans++;
            return;
        }

        backtrack(i + 1, sum + nums[i], nums);
        backtrack(i + 1, sum - nums[i], nums);
    }

    static int findTargetSumWays(int[] nums, int target) {
        backtrack(0, -target, nums);
        return ans;
    }

    public static void main(String[] args) {
        int[] nums ={1,1,1,1,1};
        int target = 3;
        System.out.println(findTargetSumWays(nums, target));
    }
}
