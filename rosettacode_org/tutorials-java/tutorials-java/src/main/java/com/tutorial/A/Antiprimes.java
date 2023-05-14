package com.tutorial.A;

public class Antiprimes {
    static int countDivisors(int n) {
        if(n < 2) return 1;
        int count = 2; // 1 and n
        for(int i = 2; i <= n / 2; ++i) {
            if(n % i == 0) ++count;
        }
        return count;
    }

    public static void main(String[] args) {
        int maxDiv = 0, count = 0;
        System.out.println("The first 20 anti-primes are:");
        for(int i = 1; count < 20; ++i) {
            int d = countDivisors(i);
            if(d > maxDiv) {
                System.out.printf("%d ", i);
                maxDiv = d;
                count++;
            }
        }
        System.out.println();
    }
}
