package com.mycompany.github.multithreading.thanhit95;

import java.util.ArrayList;
import java.util.List;

public class AppListThread001 {
    public static void main(String[] args) {
        final int NUM_THREADS = 5;

        List<Thread> lstTh = new ArrayList<Thread>();

        for(int i = 0; i < NUM_THREADS; ++i) {
            final int index = i;
            lstTh.add(new Thread( () -> {
                try { Thread.sleep(500); }
                catch(InterruptedException e) {}

                System.out.print(" " + index);
            }));
        }

//        for(Thread th : lstTh) {
//            th.start();
//        }

        // We can reduce above for loop with this statement:
        lstTh.forEach(Thread::start);
    }
}
