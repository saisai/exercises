package com.mycompany.github.multithreading.thanhit95;

public class App002 {
    static class ExampleThread extends Thread {
        @Override
        public void run() {
            System.out.println("Hello from example Thread");
        }
    }

    public static void main(String[] args) throws InterruptedException {
        ExampleThread th = new ExampleThread();
        th.run();
        System.out.println("Hello from main thread");
    }
}
