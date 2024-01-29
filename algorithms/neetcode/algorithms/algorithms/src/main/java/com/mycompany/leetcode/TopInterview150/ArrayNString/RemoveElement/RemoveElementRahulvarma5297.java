package com.mycompany.leetcode.TopInterview150.ArrayNString.RemoveElement;

public class RemoveElementRahulvarma5297 {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        for(int i = 0 ;i < nums.length; i++) {
            if(nums[i] != val) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }

    public static void main(String[] args) {
        RemoveElementRahulvarma5297 obj = new RemoveElementRahulvarma5297();
        int[] nums = new int[]{3, 2, 2, 3};
        int val = 3;

        System.out.println(obj.removeElement(nums, 3));
    }
}
