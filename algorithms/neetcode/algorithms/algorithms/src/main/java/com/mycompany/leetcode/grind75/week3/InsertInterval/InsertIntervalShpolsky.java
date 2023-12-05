package com.mycompany.leetcode.grind75.week3.InsertInterval;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Interval {
    int start;
    int end;
    public Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}
public class InsertIntervalShpolsky {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new LinkedList<>();
        int i = 0;
        // add all the intervals ending before newInterval starts
        while(i < intervals.size() && intervals.get(i).end < newInterval.start)
            result.add(intervals.get(i++));
        // merge all overlapping intervals to one considering newInterval
        while(i < intervals.size() && intervals.get(i).start <= newInterval.end) {
            newInterval = new Interval(
                    Math.min(newInterval.start, intervals.get(i).start),
                    Math.max(newInterval.end, intervals.get(i).end));
            i++;
        }
        result.add(newInterval);
        while(i < intervals.size()) result.add(intervals.get(i++));
        return result;
    }

    public static void main(String[] args) {
        List<Interval> intervals = new ArrayList<Interval>(){{
                        add(new Interval(1, 3));
                        add(new Interval(6, 9));
                }};
        Interval newInterval = new Interval(2,5);

        InsertIntervalShpolsky obj = new InsertIntervalShpolsky();
        List<Interval> result = obj.insert(intervals, newInterval);

        for(Interval interval : result) {
            System.out.println(interval.start + " " + interval.end);
        }
    }
}
