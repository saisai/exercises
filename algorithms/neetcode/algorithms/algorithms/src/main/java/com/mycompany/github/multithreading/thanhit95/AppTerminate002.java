/*
 * FORCING A THREAD TO TERMINATE (i.e. killing the thread)
 * Version B: Using a flag to notify the thread
 *
 * Beside atomic variables, you can use the "volatile" specifier.
 */

package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.atomic.AtomicBoolean;

public class AppTerminate002 {
    public static void main(String[] args) throws InterruptedException {
        AtomicBoolean flagStop = new AtomicBoolean(false);

        Thread th = new Thread(() -> {
            while(true) {
                if(flagStop.get())
                    break;

                System.out.println("Running...");

                try {Thread.sleep(100);}
                catch(InterruptedException e) {}
            }
        });

        th.start();
        Thread.sleep(3000);
        System.out.println("After sleep");
        flagStop.set(true);
    }
}
