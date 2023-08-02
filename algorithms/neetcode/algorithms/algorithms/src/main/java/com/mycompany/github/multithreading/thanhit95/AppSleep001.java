package com.mycompany.github.multithreading.thanhit95;

public class AppSleep001 {
    public static void main(String[] args) throws InterruptedException {
        Thread thFoo = new Thread(() -> {
            System.out.println("foo is sleeping");

            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {

            }
            System.out.println("foo wakes up");
        });

        thFoo.start();
        thFoo.join();

        System.out.println("Good Bye");
    }
}
