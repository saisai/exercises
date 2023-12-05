package com.mycompany.leetcode.grind75.week2.MajorityElement;

public class MajorityElementCoderoath {
    public int majorityElement(int[] num) {
        int major = num[0], count = 1;
        for(int i = 1; i < num.length; i++) {
            if(count == 0) {
                count++;
                major = num[i];
            } else if(major == num[i]) {
                count++;
            } else {
                count--;
            }
        }
        return major;
    }

    public static void main(String[] args) {
        MajorityElementCoderoath obj = new MajorityElementCoderoath();
        int[] nums = {2,2,1,1,1,2,2};
        System.out.println(obj.majorityElement(nums));
    }
}
