package com.mycompany.leetcode.TopInterview150.intervals.MinimumNumberOfArrowsToBurstBalloons;

import java.util.Arrays;

public class MinimumNumberOfArrowsToBurstBalloons150Joshua924 {
    public int findMinArrowShots(int[][] points) {
        if(points.length == 0) {
            return 0;
        }
        Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int arrowPos = points[0][1];
        int arrowCnt = 1;
        for(int i = 1; i < points.length; i++) {
            if(arrowPos >= points[i][0]) {
                continue;
            }
            arrowCnt++;
            arrowPos = points[i][1];
        }
        return arrowCnt;
    }

    public static void main(String[] args) {
        int[][] points = {{10,16},{2,8},{1,6},{7,12}};
        MinimumNumberOfArrowsToBurstBalloons150Joshua924 obj = new MinimumNumberOfArrowsToBurstBalloons150Joshua924();
        System.out.println(obj.findMinArrowShots(points));
    }
}
