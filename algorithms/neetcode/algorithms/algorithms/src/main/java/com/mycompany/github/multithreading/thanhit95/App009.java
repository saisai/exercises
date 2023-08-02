package com.mycompany.github.multithreading.thanhit95;

public class App009 {
    public static void main(String[] args) {
        Thread th = new Thread("Lorem") {
            @Override
            public void run() {
                Thread myself = Thread.currentThread(); // th is myself

                System.out.println("My name is " + this.getName()); // or myself.getName()
                System.out.println("My self is " + myself);
            }
        };

        th.start();
    }
}
