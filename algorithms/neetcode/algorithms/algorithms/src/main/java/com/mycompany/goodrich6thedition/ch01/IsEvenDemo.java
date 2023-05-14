package com.mycompany.goodrich6thedition.ch01;

public class IsEvenDemo {

    private static boolean isEven(int n) {
        while(n > 0) {
            n = n - 2;
            if(n == 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isEven(1258));
    }
}
