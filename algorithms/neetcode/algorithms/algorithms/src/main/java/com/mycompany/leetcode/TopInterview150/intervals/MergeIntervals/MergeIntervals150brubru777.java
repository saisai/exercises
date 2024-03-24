package com.mycompany.leetcode.TopInterview150.intervals.MergeIntervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class MergeIntervals150brubru777 {
    public int[][] merge(int[][] intervals) {
        if(intervals.length <= 1) {
            return intervals;
        }

        // sort by ascending starting point
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

        List<int[]> result = new ArrayList<>();
        int[] newInterval = intervals[0];
        result.add(newInterval);
        for(int[] interval : intervals) {
            if(interval[0] <= newInterval[1]) {
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            } else {
                newInterval = interval;
                result.add(newInterval);
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        MergeIntervals150brubru777 obj = new MergeIntervals150brubru777();
        int[][] intervals = {{1,3},{2,6},{8,10},{15,18}};
        int[][] result = obj.merge(intervals);
        Stream<int[]> rr = Stream.of(result);
        rr.forEach(r -> {
            System.out.println(Arrays.toString(r));
            for(int d : r) {
                System.out.print(d);
            }
        });
    }
}
