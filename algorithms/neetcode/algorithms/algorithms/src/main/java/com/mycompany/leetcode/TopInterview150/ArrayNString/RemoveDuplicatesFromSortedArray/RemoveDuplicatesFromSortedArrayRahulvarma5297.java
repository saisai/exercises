package com.mycompany.leetcode.TopInterview150.ArrayNString.RemoveDuplicatesFromSortedArray;

public class RemoveDuplicatesFromSortedArrayRahulvarma5297 {
    public int removeDuplicates(int[] nums) {
        int j = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[i - 1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }

    public static void main(String[] args) {
        int[] nums = new int[] {1,1,2};
        RemoveDuplicatesFromSortedArrayRahulvarma5297 obj = new RemoveDuplicatesFromSortedArrayRahulvarma5297();
        System.out.println(obj.removeDuplicates(nums));
    }
}
