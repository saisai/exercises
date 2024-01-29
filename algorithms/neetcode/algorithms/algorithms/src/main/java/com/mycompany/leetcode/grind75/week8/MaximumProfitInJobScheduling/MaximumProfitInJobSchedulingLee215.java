package com.mycompany.leetcode.grind75.week8.MaximumProfitInJobScheduling;

import java.util.Arrays;
import java.util.TreeMap;

public class MaximumProfitInJobSchedulingLee215 {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];
        for(int i = 0; i < n; i++) {
            jobs[i] = new int[] {startTime[i], endTime[i], profit[i]};

        }

        Arrays.sort(jobs, (a, b) -> a[1] - b[1]);
        TreeMap<Integer, Integer> dp = new TreeMap<>();
        dp.put(0, 0);
        for(int[] job: jobs) {
            int cur = dp.floorEntry(job[0]).getValue() + job[2];
            if(cur > dp.lastEntry().getValue()) {
                dp.put(job[1], cur);
            }
        }
        return dp.lastEntry().getValue();
    }

    public static void main(String[] args) {
        int[] startTime = {1,2,3,3}, endTime = {3,4,5,6}, profit = {50,10,40,70};
        MaximumProfitInJobSchedulingLee215 obj = new MaximumProfitInJobSchedulingLee215();
        System.out.println(obj.jobScheduling(startTime, endTime, profit));
    }
}
