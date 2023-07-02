package com.mycompany.leetcode.blind75.array.TwoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSumPrernadobriyal {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for(int i= 0; i < nums.length; i++) {
            if(map.containsKey(target - nums[i])) {
                result[1] = i;
                result[0] = map.get(target-nums[i]);
                break;
            }
            map.put(nums[i], i);
        }
        return result;
    }

    public static void main(String[] args) {
        TwoSumPrernadobriyal obj = new TwoSumPrernadobriyal();
        int[] nums = {2,7,11,15};
        int target = 9;

        System.out.println(obj.twoSum(nums, target));
        int[] results = obj.twoSum(nums, target);
        System.out.println(Arrays.toString(results));
    }
}

// https://leetcode.com/problems/two-sum/solutions/3464581/java-solution-using-hashmap/