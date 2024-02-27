package com.mycompany.leetcode.TopInterview150.TwoPointers.TwoSumIiInputArrayIsSorted;

import java.io.PrintStream;
import java.util.Arrays;

public class TwoSumIiInputArrayIsSortedCiote {
    public int[] twoSum(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while(nums[l] + nums[r] != target) {
            if(nums[l] + nums[r] < target) l++;
            else r --;
        }

        return new int[] {l+1, r+1};
    }

    public static void main(String[] args) {
        TwoSumIiInputArrayIsSortedCiote obj = new TwoSumIiInputArrayIsSortedCiote();
        int[] numbers = {2,7,11,15};
        int target = 9;

        System.out.println(Arrays.toString(obj.twoSum(numbers, target)));
    }
}
