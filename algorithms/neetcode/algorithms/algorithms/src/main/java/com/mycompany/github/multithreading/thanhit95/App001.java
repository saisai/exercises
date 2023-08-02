package com.mycompany.github.multithreading.thanhit95;

public class App001 {
    static class ExampleThread extends Thread {
        @Override
        public void run() {
            for(int i = 0; i < 300; i++) {
                System.out.print("B");
            }
        }
    }

    public static void main(String[] args) {
        Thread th = new ExampleThread();
        th.start();
        for(int i = 0; i < 300; ++i) {
            System.out.print("A");
        }
    }
}
