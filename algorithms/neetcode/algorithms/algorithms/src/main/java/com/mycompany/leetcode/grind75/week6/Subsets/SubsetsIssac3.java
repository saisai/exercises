package com.mycompany.leetcode.grind75.week6.Subsets;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class SubsetsIssac3 {
    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start) {
        list.add(new ArrayList<>(tempList));
        for(int i = start; i < nums.length; i++) {
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3};

        SubsetsIssac3 obj = new SubsetsIssac3();
        List<List<Integer>>  results  = obj.subsets(nums);

        results.forEach(lst -> {
            System.out.println(lst);
        });
    }

}
