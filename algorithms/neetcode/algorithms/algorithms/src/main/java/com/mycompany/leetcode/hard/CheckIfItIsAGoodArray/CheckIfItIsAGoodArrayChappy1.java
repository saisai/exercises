package com.mycompany.leetcode.hard.CheckIfItIsAGoodArray;



public class CheckIfItIsAGoodArrayChappy1 {
    static int GCD(int i,int j){
        if(j==0) return i;
        return GCD(j,i%j);
    }

    static boolean isGoodArray(int[] nums) {
        int result=nums[0];
        for(int i=1;i<nums.length;i++) {
            result=GCD(nums[i],result);
            if (result==1) return true;
        }
        return result==1;
    }

    public static void main(String[] args) {
        int[] nums = {12,5,7,23};
        System.out.println(isGoodArray(nums));
    }
}
