package com.mycompany.leetcode.blind75.array.ContainsDuplicate;

import java.util.HashSet;

public class ContainsDuplicatePratikSen07 {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hset = new HashSet<Integer>();
        for(int idx = 0; idx < nums.length; idx++) {
            if(hset.contains(nums[idx])) {
                return true;
            }
            hset.add(nums[idx]);
        }
        return false;
    }

    public boolean containsDuplicate2(int[] nums) {
        if(nums == null || nums.length == 0)
            return false;

        HashSet<Integer> hset = new HashSet<Integer>();
        for(int idx : nums) {
            if(!hset.add(idx)){
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        ContainsDuplicatePratikSen07 obj = new ContainsDuplicatePratikSen07();
        int[] nums = {1,2,3,1};
        System.out.println(obj.containsDuplicate(nums));
        System.out.println(obj.containsDuplicate2(nums));
    }
}
