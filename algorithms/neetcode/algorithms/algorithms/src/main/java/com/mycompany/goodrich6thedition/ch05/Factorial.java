package com.mycompany.goodrich6thedition.ch05;

import java.util.Scanner;

public class Factorial {

    public static int factorial(int n) {
        if(n < 0)
            throw new IllegalArgumentException();
        else if(n == 0)
            return 1;
        else
            return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("Enter a number:");
//        Scanner stdIn = new Scanner(System.in);
//        System.out.println(factorial(stdIn.nextInt()));
        System.out.println(factorial(5));
    }

}
