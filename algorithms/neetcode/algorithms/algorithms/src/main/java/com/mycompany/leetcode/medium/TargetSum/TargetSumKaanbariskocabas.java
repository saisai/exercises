package com.mycompany.leetcode.medium.TargetSum;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class TargetSumKaanbariskocabas {

    static void backtrack(int i, int sum, LinkedList<Integer> cur, int[] nums, List<List<Integer>> res) {
        if(i == nums.length) {
            if(sum == 0) {
                res.add(new ArrayList<>(cur));
            }
            return;
        }

        cur.addLast(nums[i]);
        backtrack(i + 1, sum + nums[i], cur, nums, res);
        cur.removeLast();
        cur.addLast(-nums[i]);
        backtrack(i + 1, sum - nums[i], cur, nums, res);
        cur.removeLast();
    }
    static int findTargetSumWays(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, -target, new LinkedList<>(), nums, res);
        System.out.println(res);
        return res.size();

    }

    public static void main(String[] args) {
        int[] nums ={1,1,1,1,1};
        int target = 3;
        System.out.println(findTargetSumWays(nums, target));
    }


}
