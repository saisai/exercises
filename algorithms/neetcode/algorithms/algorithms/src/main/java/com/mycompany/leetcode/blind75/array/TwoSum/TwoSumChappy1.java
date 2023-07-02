package com.mycompany.leetcode.blind75.array.TwoSum;

import java.util.Arrays;

public class TwoSumChappy1 {
    public int[] twoSum(int[] nums, int target) {
        for(int i =1; i < nums.length;i++) {
            for(int j = i; j < nums.length; j++) {
                if(nums[j] + nums[j - 1] == target) {
                    return new int[] {j-i, j};
                }
            }
        }
        return null;
    }

    public static void main(String[] args) {

        int[] nums = {2,7,11,15};
        int target = 9;
        TwoSumChappy1 obj = new TwoSumChappy1();
        System.out.println(Arrays.toString(obj.twoSum(nums, target)));

    }
}
// https://leetcode.com/problems/two-sum/solutions/3140107/solution/