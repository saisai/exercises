package com.mycompany.github.multithreading.thanhit95;

public class App004 {
    public static void main(String[] args) {

        Runnable doTask = () -> System.out.println("Hello from example thread");

        Thread th1 = new Thread(doTask);
        Thread th2 = new Thread(doTask);
        th1.start();
        th2.start();

        System.out.println("Hello from main thread");
    }


}
