package com.mycompany.goodrich6thedition.ch01;

import java.util.Scanner;

public class IsMultipleDemo {
    private static boolean isMultiple(long n, long m) {
        if(m > n) {
            return isMultiple(m, n);
        }
        return n % m == 0;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.println("Please input two numbers for n and m:");
        long n = stdIn.nextLong();
        long m = stdIn.nextLong();
        System.out.println(isMultiple(n, m));
    }
}
