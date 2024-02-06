package com.mycompany.leetcode.TopInterview150.ArrayNString.JumpGameIi;

public class JumpGameIiChengZhang {
    public int jump(int[] nums) {
        int jumps = 0, curEnd = 0, curFarthest = 0;
        for(int i = 0; i < nums.length - 1; i++) {
            curFarthest = Math.max(curFarthest, i + nums[i]);
            if(i == curEnd) {
                jumps++;
                curEnd = curFarthest;
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        JumpGameIiChengZhang obj = new JumpGameIiChengZhang();
        int[] nums = {2,3,1,1,4};
        System.out.println(obj.jump(nums));
    }
}
