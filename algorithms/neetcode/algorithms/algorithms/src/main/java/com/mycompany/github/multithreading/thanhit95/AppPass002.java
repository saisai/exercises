package com.mycompany.github.multithreading.thanhit95;

public class AppPass002 {

    private static void doTask(int a, double b, String c) {
        System.out.printf("%d %.1f %s %n", a, b, c);
    }

    public static void main(String[] args) {
        Thread thFoo = new Thread(() -> doTask(1, 2, "Red"));
        Thread thBar = new Thread(() -> doTask(3, 4, "blue"));

        thFoo.start();
        thBar.start();
    }
}
