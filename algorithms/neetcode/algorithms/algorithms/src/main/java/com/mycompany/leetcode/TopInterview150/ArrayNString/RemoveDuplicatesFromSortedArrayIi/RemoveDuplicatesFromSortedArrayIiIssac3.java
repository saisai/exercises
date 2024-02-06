package com.mycompany.leetcode.TopInterview150.ArrayNString.RemoveDuplicatesFromSortedArrayIi;

public class RemoveDuplicatesFromSortedArrayIiIssac3 {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for(int n : nums) {
            if(i < 2 || n > nums[i - 2]) {
                nums[i++] = n;
            }
        }
        return i;
    }
    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArrayIiIssac3 obj = new RemoveDuplicatesFromSortedArrayIiIssac3();
        int[] nums = {1,1,1,2,2,3};
        System.out.println(obj.removeDuplicates(nums));
    }
}
