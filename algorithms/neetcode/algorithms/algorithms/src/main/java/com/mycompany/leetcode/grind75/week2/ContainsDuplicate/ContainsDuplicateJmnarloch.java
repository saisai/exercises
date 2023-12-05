package com.mycompany.leetcode.grind75.week2.ContainsDuplicate;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicateJmnarloch {
    public boolean containsDuplicate(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean containsDuplicate2(int[] nums) {
        Arrays.sort(nums);
        for(int ind = 1; ind < nums.length; ind++) {
            if(nums[ind] == nums[ind - 1]) {
                return true;
            }
        }
        return false;
    }

    public boolean containsDuplicateHashSet(int[] nums) {
        Set<Integer> distinct = new HashSet<Integer>();
        for(int num : nums) {
            if(distinct.contains(num)) {
                return true;
            }
            distinct.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1,3,3,4,3,2,4,2};
        ContainsDuplicateJmnarloch obj = new ContainsDuplicateJmnarloch();
        System.out.println(obj.containsDuplicate(nums));
        System.out.println(obj.containsDuplicate2(nums));
        System.out.println(obj.containsDuplicateHashSet(nums));
    }
}
