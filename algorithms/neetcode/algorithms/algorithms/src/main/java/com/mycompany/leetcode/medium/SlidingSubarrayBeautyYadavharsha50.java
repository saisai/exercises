package com.mycompany.leetcode.medium;

import java.util.Arrays;

// https://leetcode.com/problems/sliding-subarray-beauty/solutions/3446401/count-frequency/
public class SlidingSubarrayBeautyYadavharsha50 {
    private static int getSmallest(int freq[], int k, int x) {
        for(int i = 0 ; i < 50; i++) {
            if(freq[i] > 0) {
                x -= freq[i];
                if(x <= 0) return i - 50;
            }
        }
        return 0;
    }

    private static int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int freq[] = new int[50];
        int res[] = new int[nums.length -k + 1];
        int j = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] < 0) freq[nums[i]+50]++;
            if(i-k >= 0 && nums[i-k] < 0) freq[nums[i-k]+50]--;
            if(i - k + 1 >= 0) res[j++] = getSmallest(freq, k, x);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,-1,-3,-2,3};
        int k = 3, x = 2;
        System.out.println(Arrays.toString(getSubarrayBeauty(nums,k, x)));
    }
}
