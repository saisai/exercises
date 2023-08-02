package com.mycompany.github.multithreading.thanhit95;

public class AppTerminate001 {
    public static void main(String[] args) throws InterruptedException {
        Thread th = new Thread(() -> {
            while(true) {
                System.out.println("Running...");

                try {Thread.sleep(100);}
                catch (InterruptedException e) {
                    // Received interrupt signal, now current thread is going to exit
                    return;
                }
            }
        });

        th.start();

        Thread.sleep(3000);
        System.out.println("After sleep");
        th.interrupt();
    }
}
