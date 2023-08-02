package com.mycompany.github.multithreading.thanhit95;

public class App003 {
    public static void main(String[] args) {
        Thread th = new Thread() {
            @Override
            public void run() {
                System.out.println("Hello from example thread");
            }
        };

        th.start();

        System.out.println("Hello from main thread");
    }
}
