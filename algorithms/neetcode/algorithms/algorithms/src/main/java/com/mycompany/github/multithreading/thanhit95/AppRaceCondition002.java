package com.mycompany.github.multithreading.thanhit95;

import java.util.Arrays;

/*
 * DATA RACES
 * Version 01: Without multithreading
 */

public class AppRaceCondition002 {
    private static int getResult(int N) {
        boolean[] a = new boolean[N + 1];
        Arrays.fill(a, false);

        for(int i= 1; i <= N; ++i) {
            if(i % 2 == 0 || i % 3 == 0) {
                a[i] = true;
            }
        }

        int res = countTrue(a, N);
        return res;
    }

    private static int countTrue(boolean[] a, int N) {
        int count = 0;
        for(int i = 1; i <= N; ++i) {
            if(a[i]) {
                ++count;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        final int N = 8;
        int result = getResult(N);
        System.out.println("Number of integers that are divisible by 2 or 3 is: " + result);
    }
}
