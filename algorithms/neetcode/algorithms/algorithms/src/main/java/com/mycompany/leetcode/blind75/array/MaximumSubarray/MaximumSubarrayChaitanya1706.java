package com.mycompany.leetcode.blind75.array.MaximumSubarray;

public class MaximumSubarrayChaitanya1706 {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int max = Integer.MIN_VALUE, sum = 0;

        for(int i = 0; i < n; i++) {
            sum += nums[i];
            max = Math.max(sum, max);

            if(sum < 0) sum = 0;
        }
        return max;
    }

    public static void main(String[] args) {
        MaximumSubarrayChaitanya1706 obj = new MaximumSubarrayChaitanya1706();
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(obj.maxSubArray(nums));
    }

}
