package com.mycompany.github.multithreading.thanhit95;

import java.util.List;
import java.util.stream.IntStream;

public class AppListThread002 {
    public static void main(String[] args) {
        List<Thread> lstTh = IntStream.range(0, 5).mapToObj(i -> new Thread(() -> {
            try { Thread.sleep(500);}
            catch( InterruptedException e) {}

            System.out.print(" " + i);
        })).toList();

        for(Thread th : lstTh)
            th.start();

        // We can reduce above for loop with this statement:
        // lstTh.forEach(Thread::start);
    }
}
