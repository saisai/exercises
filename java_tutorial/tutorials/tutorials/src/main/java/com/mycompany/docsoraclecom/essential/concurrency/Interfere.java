package com.mycompany.docsoraclecom.essential.concurrency;

public class Interfere {

    static class Counter {
        private int c = 0;

        public void increment() {
            c++;
        }

        public void decrement() {
            c--;
        }

        public int value() {
            return c;
        }
    }

    static void printThread(int value) {
        String currentThread = Thread.currentThread().getName();
        System.out.printf("Current thread %s and its value %d%n ", currentThread, value);
    }
    public static void main(String[] args) {

        Counter c = new Counter();

        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                printThread(c.value());
                c.increment();
                printThread(c.value());

            }
        });

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                printThread(c.value());
                c.decrement();
                printThread(c.value());

            }
        });

        t1.start();
        t2.start();

    }
}
