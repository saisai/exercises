package com.mycompany.github.multithreading.thanhit95;

public class App007 {
    private static void doTask() {
        System.out.println("Hello from example thread");
    }

    public static void main(String[] args) {
        Thread th = new Thread(App007::doTask);
        th.start();
        System.out.println("Hello from main thread");
    }
}
