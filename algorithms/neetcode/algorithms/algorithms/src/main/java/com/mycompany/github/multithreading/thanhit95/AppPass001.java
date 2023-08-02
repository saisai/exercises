package com.mycompany.github.multithreading.thanhit95;

public class AppPass001 {
    static class MyThread extends Thread {
        private  int a;
        private double b;
        private String c;
        public  MyThread(int a, double b, String c) {
            super();
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public void run() {
            System.out.printf("%d %.1f %s %n", a, b, c);
        }
    }

    public static void main(String[] args) {
        Thread thFoo = new MyThread(1, 2, "red");
        Thread thBar = new MyThread(3, 4, "blue");
        thFoo.start();
        thBar.start();
    }
}
