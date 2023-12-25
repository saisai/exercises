package com.mycompany.leetcode.grind75.week5.SortColors;

import java.util.Arrays;

public class SortColorsShichaotan {
    public void sortColors(int[] A, int n) {
        int n0 = -1, n1 = -1, n2 = -1;
        for(int i = 0; i < n; i++) {
            if(A[i] == 0) {
                A[++n2] = 2;
                A[++n1] = 1;
                A[++n0] = 0;
            } else if(A[i] == 1) {
                A[++n2] = 2;
                A[++n1] = 1;
            } else if(A[i] == 2) {
                A[++n2] = 2;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {2,0,2,1,1,0};
        SortColorsShichaotan obj = new SortColorsShichaotan();
        obj.sortColors(nums, nums.length);
        System.out.println(Arrays.toString(nums));
    }
}
