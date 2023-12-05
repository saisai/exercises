package com.mycompany.leetcode.grind75.week1.TwoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSumKshatriyas {
    public int[] twoSumBruteForce(int[] nums, int target) {
        int n = nums.length;
        for(int i = 0; i < n - 1; i++) {
            for(int j = i + 1; j < n; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{};
    }

    public int[] twoSumTowPassHashTable(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        // build the hash table
        for(int i = 0; i < n; i++) {
            numMap.put(nums[i], i);
        }

        for(int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if(numMap.containsKey(complement) && numMap.get(complement) != i) {
                return new int[]{i, numMap.get(complement)};
            }
        }

        return new int[]{};
    }

    public int[] twoSumOnePassHashTable(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for(int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if(numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            numMap.put(nums[i], i);
        }
        return new int[]{};
    }
    public static void main(String[] args) {
        TwoSumKshatriyas obj = new TwoSumKshatriyas();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] results = obj.twoSumBruteForce(nums, target);
        System.out.print(Arrays.toString(results));

        int[] results2 = obj.twoSumTowPassHashTable(nums, target);
        System.out.print(Arrays.toString(results2));

        int[] results3 = obj.twoSumOnePassHashTable(nums, target);
        System.out.print(Arrays.toString(results3));
    }
}
