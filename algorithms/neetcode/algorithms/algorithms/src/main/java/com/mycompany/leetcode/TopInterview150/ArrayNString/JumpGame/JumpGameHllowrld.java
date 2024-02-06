package com.mycompany.leetcode.TopInterview150.ArrayNString.JumpGame;

public class JumpGameHllowrld {
    public boolean canJump(int[] nums) {
        int reachable = 0;
        for(int i = 0; i < nums.length; ++i) {
            if(i > reachable) return false;
            reachable = Math.max(reachable, i + nums[i]);
        }
        return true;
    }

    public static void main(String[] args) {
        JumpGameHllowrld obj = new JumpGameHllowrld();
        int[] nums = {2,3,1,1,4};
        System.out.println(obj.canJump(nums));
    }
}
