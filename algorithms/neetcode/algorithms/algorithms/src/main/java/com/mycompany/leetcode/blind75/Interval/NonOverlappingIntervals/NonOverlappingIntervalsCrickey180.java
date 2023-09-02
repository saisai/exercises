package com.mycompany.leetcode.blind75.Interval.NonOverlappingIntervals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class NonOverlappingIntervalsCrickey180 {
    static class Interval {
        private int start;
        private int end;

        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    static int eraseOverlapIntervals(Interval[] intervals) {
        if(intervals.length == 0) return 0;

        Arrays.sort(intervals, new myComparator());
        int end = intervals[0].end;
        int count = 1;

        for(int i = 1; i < intervals.length; i++) {
            if(intervals[i].start >= end) {
                end = intervals[i].end;
                count++;
            }
        }
        return intervals.length - count;
    }

    static class myComparator implements Comparator<Interval> {

        @Override
        public int compare(Interval a, Interval b) {
            return a.end - a.start;
        }
    }

    public static void main(String[] args) {
//        List<Interval> intervals = new ArrayList<>(){{
//            new Interval(1, 2);
//            new Interval(2, 3);
//            new Interval(3, 4);
//            new Interval(1, 3);
//        }};

        Interval[] intervals = {
                            new Interval(1, 2),
                            new Interval(2, 3),
                            new Interval(3, 4),
                            new Interval(1, 3)
        };
        System.out.println(eraseOverlapIntervals(intervals));
    }
}
