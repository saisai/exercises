package com.mycompany.leetcode.blind75.Interval.InsertInterval;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class InsertIntervalShpolsky {

    static class Interval {
        private int start;
        private int end;

        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public String toString() {

            return "[" + start + "," + end + "]";
        }


    }

    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new LinkedList<>();
        int i = 0;
        // add all the intervals ending before newInerval starts
        while(i < intervals.size() && intervals.get(i).end < newInterval.start)
            result.add(intervals.get(i++));

        // merge all overlapping intervals to one considering newInterval
        while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
            newInterval = new Interval( // we could mutate newInterval here also
                    Math.min(newInterval.start, intervals.get(i).start),
                    Math.max(newInterval.end, intervals.get(i).end));
            i++;
        }
        result.add(newInterval); // add the union of intervals we got
        // add all the rest
        while (i < intervals.size()) result.add(intervals.get(i++));
        return result;

    }

    public static void main(String[] args) {
        List<Interval> intervals = new ArrayList<>(){{
            add(new Interval(1, 3));
            add(new Interval(6, 9));
        }};

        Interval newInterval = new Interval(2,5);
        InsertIntervalShpolsky obj = new InsertIntervalShpolsky();
        List<Interval> result;
        result = obj.insert(intervals, newInterval);
        for(Interval val : result) {
            System.out.print(val);
        }
        result.forEach(r -> System.out.println(r.start + ", " + r.end));
    }
}
