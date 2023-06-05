package com.mycompany.leetcode.easy.DuplicateZeros;

import java.util.Arrays;

public class DuplicateZerosChappy1 {

    static void duplicateZeros(int[] arr) {
        int[] ans = new int[arr.length];
        int j = 0;
        for(int i = 0; i < arr.length && j < arr.length; i++) {
            if(arr[i] == 0 && j < arr.length - 1) {
                ans[j] = 0;
                ans[j + 1] = 0;
                j = j + 2;
            } else {
                ans[j++] = arr[i];
            }
        }
        System.out.println(Arrays.toString(ans));
        System.arraycopy(ans, 0, arr, 0, arr.length);
        System.out.println(Arrays.toString(ans));
    }

    public static void main(String[] args) {
        int[] arr = {1,0,2,3,0,4,5,0};

        duplicateZeros(arr);
    }
}
