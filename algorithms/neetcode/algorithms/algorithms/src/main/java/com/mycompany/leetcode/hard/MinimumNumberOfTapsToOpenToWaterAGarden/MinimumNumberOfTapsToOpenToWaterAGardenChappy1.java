package com.mycompany.leetcode.hard.MinimumNumberOfTapsToOpenToWaterAGarden;

public class MinimumNumberOfTapsToOpenToWaterAGardenChappy1 {
    static int minTaps(int n, int[] ranges) {
        for(int idx = 0; idx <= n; idx++) {
            int start = Math.max(0, idx - ranges[idx]);
            int end = Math.min(n, idx + ranges[idx]);
            ranges[start] = end - start;
        }

        if(ranges[0] == 0) return -1;
        int laddres = ranges[0];
        int stairs = ranges[0];
        int minJumps = 1;

        for(int idx = 1; idx <= n; idx++) {
            if(idx == n) return minJumps;

            if(idx + ranges[idx] > laddres) laddres = idx + ranges[idx];

            stairs--;
            if(stairs == 0) {
                if(laddres <= idx) return -1;

                stairs = laddres - idx;
                minJumps++;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int n = 5;
        int[] ranges = {3,4,1,1,0,0};

        System.out.println(minTaps(n, ranges));
    }
}
