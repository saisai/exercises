package com.mycompany.leetcode.blind75;

import com.mycompany.leetcode.medium.MakeCostsOfPathsEqualInABinaryTreeHobiter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InsertIntervalShpolsky {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if(intervals.length == 0) return new int[][]{newInterval};
        List<int[]> rst = new ArrayList<>();
        int i = 0, n = intervals.length;
        while(i < n && intervals[i][1] < newInterval[0]) {
            rst.add(intervals[i]);
            ++i;
        }

        while(i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][0], newInterval[1]);
            ++i;
        }

        rst.add(newInterval);
        while(i < n) {
            rst.add(intervals[i]);
            ++i;
        }
        return rst.toArray(new int[rst.size()][]);
    }

    public static void main(String[] args) {
        InsertIntervalShpolsky obj = new InsertIntervalShpolsky();
        int[][] intervals = {{1,3},{6,9}};
        int[] newInterval = {2,5};
        System.out.println(obj.insert(intervals, newInterval));
        System.out.println(Arrays.deepToString(obj.insert(intervals, newInterval)));
    }
}

 // https://leetcode.com/zhqyvvn/
// https://leetcode.com/problems/insert-interval/solutions/21602/short-and-straight-forward-java-solution/
// https://stackoverflow.com/questions/19648240/the-best-way-to-print-a-java-2d-array
