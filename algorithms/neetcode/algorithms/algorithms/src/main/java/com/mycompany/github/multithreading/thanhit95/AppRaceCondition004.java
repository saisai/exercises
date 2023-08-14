/*
 * RACE CONDITIONS AND DATA RACES
 */


package com.mycompany.github.multithreading.thanhit95;

import java.util.List;
import java.util.stream.Stream;

public class AppRaceCondition004 {
    private static class Global {
        public static int counter = 0;
    }

    public static void main(String[] args) throws InterruptedException {
        final int NUM_THREADS = 16;

        List<Thread> lstTh = (List<Thread>) Stream.generate(() -> new Thread(() -> {

            try { Thread.sleep(1000); } catch (InterruptedException e) { }

            for (int i = 0; i < 1000; ++i) {
                Global.counter += 1;
            }

        })).limit(NUM_THREADS).toList();

        for(Thread th : lstTh) {
            th.start();
        }

        for(Thread th : lstTh) {
            th.join();
        }

        System.out.println("counter = " + Global.counter);
        /*
         * We are not sure that counter = 16000
         */
    }

}
