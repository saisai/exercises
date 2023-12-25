package com.mycompany.leetcode.grind75.week5.Permutations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PermutationsHieroglyphs {
    public List<List<Integer>> recursiveBacktracking(List<Integer> numsList, List<List<Integer>> res, List<Integer> path) {
        if(numsList.isEmpty()) {
            res.add(new ArrayList<>(path));
        } else {
            for(int i = 0; i < numsList.size(); i++) {
                List<Integer> newNumsLst = new ArrayList<>(numsList);
                newNumsLst.remove(i);
                path.add(numsList.get(i));
                recursiveBacktracking(newNumsLst, res, path);
                path.remove(path.size() - 1);
            }
        }
        return res;
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();

        // convert array to list
        List<Integer> numLst = new ArrayList<Integer>();
        for(int num : nums) {
            numLst.add(num);
        }

        return recursiveBacktracking(numLst, res, path);
    }
    public static void main(String[] args) {

        int[] nums = {1,2,3};
        PermutationsHieroglyphs obj = new PermutationsHieroglyphs();
        List<List<Integer>> res = obj.permute(nums);

        res.stream().forEach( lst -> {
            System.out.println(lst);
            for(int d : lst) {
                System.out.print(d);
            }
            System.out.println();
        });


    }
}
