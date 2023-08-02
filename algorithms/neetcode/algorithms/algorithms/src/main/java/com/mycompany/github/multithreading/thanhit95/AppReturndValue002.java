package com.mycompany.github.multithreading.thanhit95;

public class AppReturndValue002 {
    static int doubleValue(int value) {
        return value * 2;
    }

    public static void main(String[] args) throws InterruptedException {
        int[] result = new int[2];

        Thread thFoo = new Thread(() -> result[0] = doubleValue(5));
        Thread thBar = new Thread(() -> result[1] = doubleValue(80));

        thFoo.start();
        thBar.start();

        thFoo.join();
        thBar.join();

        // Wait until thFoo and thBar finish
        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}
