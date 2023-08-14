package com.mycompany.leetcode.blind75.graph.LongestConsecutiveSequence;

import java.util.HashMap;
import java.util.Map;

public class LongestConsecutiveSequenceDchen0215 {
    public int longestConsecutive(int[] num) {
        int res = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int n : num) {
            if(!map.containsKey(n)) {
                int left = (map.containsKey(n - 1)) ? map.get(n - 1) : 0;
                int right = (map.containsKey(n + 1)) ? map.get(n + 1) : 0;
                // sum : lenght of the sequence n is in
                int sum = left + right + 1;
                map.put(n, sum);

                // keep track of the max length
                res = Math.max(res, sum);

                // extend the length to the boundary(s)
                // of the sequence
                // will do nothing if n has no neighbors

            } else {
                // duplicates
                continue;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequenceDchen0215 obj = new LongestConsecutiveSequenceDchen0215();

        int[] nums = {100,4,200,1,3,2};

        System.out.print(obj.longestConsecutive(nums));
    }
}
