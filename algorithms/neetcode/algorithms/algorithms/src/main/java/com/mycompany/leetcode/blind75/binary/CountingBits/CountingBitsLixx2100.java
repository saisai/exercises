package com.mycompany.leetcode.blind75.binary.CountingBits;

import java.util.Arrays;

public class CountingBitsLixx2100 {
    public static int[] countBits(int num) {
        int[] f = new int[num + 1];
        for(int i = 1; i <= num; i++) f[i] = f[i >> 1] + (i & 1);
        return f;
    }

    public static void main(String[] args) {
        int[] result = countBits(5);
        System.out.println(Arrays.toString(result));
    }
}
