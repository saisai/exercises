package com.mycompany.leetcode.TopInterview150.HashMap.TwoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum150rahulvarma5297 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for(int i = 0; i < n; i++) {
            numMap.put(nums[i], i);
        }

        numMap.forEach((key, val) -> {
            System.out.println(key + ", " + val);
        });

        for(int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if(numMap.containsKey(complement) && numMap.get(complement) != i) {
                return new int[] {i, numMap.get(complement)};
            }
        }
        return new int []{};
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;

        TwoSum150rahulvarma5297 obj = new TwoSum150rahulvarma5297();
        int[] result = obj.twoSum(nums, target);

        System.out.println(Arrays.toString(result));
    }
}
