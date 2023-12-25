package org.rosettacode.learning.A.AscendingPrimes;

import java.util.Arrays;
import java.util.Map;

public class AscendingPrimes implements Runnable {

    public void run() {
        final int MAX_SIZE = 1000;
        final int[] queue = new int[MAX_SIZE];
        int begin = 0;
        int end = 0;

        for(int k = 1; k <= 9; k++) {
            queue[end++] = k;
        }

        while(begin < end) {
            int n = queue[begin++];
            for(int k = n % 10 + 1; k <= 9; k++) {
                queue[end++] = n * 10 + k;
            }
        }

        // We can use a parallel stream (and then sort the results)
        // to use multiple cores.
        //
        System.out.println(Arrays.stream(queue).filter(this::isPrime).boxed().toList());
    }

    private boolean isPrime(int n) {
        if(n == 2) {
            return true;
        }
        if(n == 1 || n % 2 == 0) {
            return false;
        }
        int root = (int) Math.sqrt(n);
        for(int k = 3; k <= root; k +=2) {
            if(n % k == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        long t1 = System.nanoTime();
        new AscendingPrimes().run();
        long t2 = System.nanoTime();
        System.out.println(
                "total time consumed = " + (t2 - t1) * 1E-6 + " milliseconds");
    }
}
