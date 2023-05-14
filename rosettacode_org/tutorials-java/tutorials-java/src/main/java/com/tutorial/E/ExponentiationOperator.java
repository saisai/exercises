package com.tutorial.E;

public class ExponentiationOperator {

    public static double pow(double base, int exp) {
        if(exp < 0) return 1 / pow(base, -exp);
        double ans = 1.0;
        for(; exp > 0; --exp) ans *= base;
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(pow(2, 30));
        System.out.println(pow(2.0, 30));
        System.out.println(pow(2.0, -2));
    }
}
