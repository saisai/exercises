package com.mycompany.github.multithreading.thanhit95;

public class AppReturndValue001 {
    static class MyThread extends Thread {
        public int arg = 0;
        public int result = 0;

        public MyThread(int arg) {
            super();
            this.arg = arg;
        }

        @Override
        public void run() {
            result = arg * 2;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread thFoo = new MyThread(5);
        Thread thBar = new MyThread(80);

        thFoo.start();
        thBar.start();

        thFoo.join();
        thBar.join();

        System.out.println(((MyThread) thFoo).result);
        System.out.println(((MyThread) thBar).result);
    }
}
