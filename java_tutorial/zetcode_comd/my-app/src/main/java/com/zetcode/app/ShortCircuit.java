package com.zetcode.app;

public class ShortCircuit {

    public static boolean One() {
        System.out.println("Inside one");
        return false;
    }

    public static boolean Two() {
        System.out.println("Inside two");
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Short circuit");

        if(One() && Two()) {
            System.out.println("Pass");
        }

        System.out.println("#########");

        if (One() || Two()) {

            System.out.println("Pass");
        }
    }
}
