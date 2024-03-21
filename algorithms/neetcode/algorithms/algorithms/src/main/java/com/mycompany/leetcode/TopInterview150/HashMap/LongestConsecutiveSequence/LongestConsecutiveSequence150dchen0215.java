package com.mycompany.leetcode.TopInterview150.HashMap.LongestConsecutiveSequence;

import java.util.HashMap;

public class LongestConsecutiveSequence150dchen0215 {
    public int longestConsecutive(int[] num) {
        int res = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int n : num) {
            if(!map.containsKey(n)) {
                int left = (map.containsKey(n - 1)) ? map.get(n - 1) : 0;
                int right = (map.containsKey(n + 1)) ? map.get(n + 1) : 0;
                int sum = left + right + 1;
                map.put(n, sum);

                res = Math.max(res, sum);

                map.put(n - left, sum);
                map.put(n + right, sum);
            } else {
                continue;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {100,4,200,1,3,2};
        LongestConsecutiveSequence150dchen0215 obj = new LongestConsecutiveSequence150dchen0215();
        System.out.println(obj.longestConsecutive(nums));
    }
}
