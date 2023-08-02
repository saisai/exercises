package com.mycompany.github.multithreading.thanhit95;

public class AppDetach001 {
    public static void main(String[] args) throws InterruptedException {
        var thFoo = new Thread(() -> {
            System.out.println("foo is starting...");

            try { Thread.sleep(2000); } catch (InterruptedException e) { }

            System.out.println("foo is exiting...");
        });


        thFoo.setDaemon(true);
        thFoo.start();


        // If I comment this statement,
        // thFoo will be forced into terminating with main thread
        Thread.sleep(3000);


        System.out.println("Main thread is exiting");
    }

}
