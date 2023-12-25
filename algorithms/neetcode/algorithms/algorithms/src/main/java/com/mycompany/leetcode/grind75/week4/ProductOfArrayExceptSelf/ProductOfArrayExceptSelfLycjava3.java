package com.mycompany.leetcode.grind75.week4.ProductOfArrayExceptSelf;

public class ProductOfArrayExceptSelfLycjava3 {
    public int[] productExeptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = 1;
        for(int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int right = 1;
        for(int i = n  - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        ProductOfArrayExceptSelfLycjava3 obj = new ProductOfArrayExceptSelfLycjava3();
        System.out.println(obj.productExeptSelf(nums));
    }
}
