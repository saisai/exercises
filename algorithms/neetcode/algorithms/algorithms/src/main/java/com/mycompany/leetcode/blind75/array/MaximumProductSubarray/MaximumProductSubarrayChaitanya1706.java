package com.mycompany.leetcode.blind75.array.MaximumProductSubarray;

public class MaximumProductSubarrayChaitanya1706 {
    public int maxProduct1(int[] nums) {
        int max = nums[0], min = nums[0], ans = nums[0];

        for(int i = 1; i < nums.length; i++) {
            int temp = max;

            max = Math.max(Math.max(max * nums[i], min * nums[i]), nums[i]);
            min = Math.min(Math.min(temp * nums[i], min * nums[i]), nums[i]);

            if(max > ans) {
                ans = max;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
       int[] nums = {2,3,-2,4};
       MaximumProductSubarrayChaitanya1706 obj = new MaximumProductSubarrayChaitanya1706();
       System.out.println(obj.maxProduct1(nums));
    }
}
