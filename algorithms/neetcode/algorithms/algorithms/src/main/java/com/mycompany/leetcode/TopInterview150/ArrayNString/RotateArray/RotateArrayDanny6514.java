package com.mycompany.leetcode.TopInterview150.ArrayNString.RotateArray;

import java.util.Arrays;

public class RotateArrayDanny6514 {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while(start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] =  temp;
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6,7};
        int k = 3;

        RotateArrayDanny6514 obj = new RotateArrayDanny6514();
        obj.rotate(nums, k);
        System.out.println(Arrays.toString(nums));
    }
}
