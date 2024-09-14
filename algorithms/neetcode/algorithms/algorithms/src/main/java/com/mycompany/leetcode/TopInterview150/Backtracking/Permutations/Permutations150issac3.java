package com.mycompany.leetcode.TopInterview150.Backtracking.Permutations;

import java.util.ArrayList;
import java.util.List;

public class Permutations150issac3 {
    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums) {
        if(tempList.size() == nums.length) {
            list.add(new ArrayList<>(tempList));
        } else {
            for(int i = 0; i < nums.length; i++) {
                if(tempList.contains(nums[i])) continue;
                tempList.add(nums[i]);
                backtrack(list, tempList, nums);
                tempList.remove(tempList.size() - 1);
            }
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        // Arrays.sort(nums); // not necessary
        backtrack(list, new ArrayList<>(), nums);
        return list;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3};
        Permutations150issac3 obj  = new Permutations150issac3();
        List<List<Integer>> results = obj.permute(nums);
        results.forEach(data -> System.out.println(data));
    }
}
