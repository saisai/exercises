package com.mycompany.leetcode.TopInterview150.Backtracking.Combinations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Combinations150fabrizio3 {
    public static void combine(List<List<Integer>> combs, List<Integer> comb, int start, int n, int k) {
        if(k == 0) {
            combs.add(new ArrayList<Integer>(comb));
            return;
        }
        for(int i = start; i <= n; i++) {
            comb.add(i);
            combine(combs, comb, i + 1, n, k - 1);
            comb.remove(comb.size() - 1);
        }
    }

    public static List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> combs = new ArrayList<List<Integer>>();
        combine(combs, new ArrayList<Integer>(), 1, n, k);
        return combs;
    }

    public static void main(String[] args) {
        Combinations150fabrizio3 obj = new Combinations150fabrizio3();
        int n = 4, k = 2;
        List<List<Integer>> results = combine(n, k);
        results.forEach(obj2 -> {
            System.out.println(Arrays.toString(obj2.toArray()));
//            for(Integer d : obj2) {
//                System.out.println(d);
//            }
        });
    }
}