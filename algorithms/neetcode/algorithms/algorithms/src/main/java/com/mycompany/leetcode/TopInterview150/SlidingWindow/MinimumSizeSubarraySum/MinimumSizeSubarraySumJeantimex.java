package com.mycompany.leetcode.TopInterview150.SlidingWindow.MinimumSizeSubarraySum;

public class MinimumSizeSubarraySumJeantimex {
    public int minSubArrayLen(int s, int[] a) {
        if(a == null || a.length == 0)
            return 0;

        int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;

        while( j < a.length) {
            sum += a[j++];

            while(sum >= s) {
                min = Math.min(min, j - i);
                sum -= a[i++];
            }
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }

    public static void main(String[] args) {
        int target = 7;
        int[] nums = {2,3,1,2,4,3};
        MinimumSizeSubarraySumJeantimex obj = new MinimumSizeSubarraySumJeantimex();
        System.out.println(obj.minSubArrayLen(target, nums));
    }
}
