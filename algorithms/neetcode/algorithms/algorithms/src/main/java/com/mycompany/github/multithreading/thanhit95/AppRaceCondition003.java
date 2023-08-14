package com.mycompany.github.multithreading.thanhit95;

import java.util.Arrays;

/*
 * DATA RACES
 * Version 02: Multithreading
 */


public class AppRaceCondition003 {
    private static int countTrue(boolean[] a, int N) {
        int count = 0;

        for (int i = 1; i <= N; ++i)
            if (a[i])
                ++count;

        return count;
    }

    public static void main(String[] args) throws InterruptedException {
        final int N = 8;

        boolean[] a = new boolean[N + 1];
        Arrays.fill(a, false);

        Thread thDiv2 = new Thread(() -> {
            for(int i = 2; i <= N; i += 2) {
                a[i] = true;
            }
        });

        Thread thDiv3 = new Thread(() -> {
            for(int i = 3; i <= N; i += 3) {
                a[i] = true;
            }
        });

        thDiv2.start();
        thDiv3.start();
        thDiv2.join();
        thDiv3.join();

        int result = countTrue(a, N);

        System.out.println("Number of integers that are divisible by 2 or 3 is: " + result);
    }
}
