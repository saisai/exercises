package com.mycompany.leetcode.medium.FindTheValueOfThePartition;

import java.util.Arrays;

public class FindTheValueOfThePartition0x4C0DE {
    public static void main(String[] args) {
        int[] nums = {1,3,2,4};
        System.out.println(findValueOfPartition(nums));
    }

    static int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);

        int value = Integer.MAX_VALUE;
        for(int i = 0; i < nums.length - 1; i++) {
            value = Math.min(value, nums[i + 1] - nums[i]);
        }

        return value;
    }
}
