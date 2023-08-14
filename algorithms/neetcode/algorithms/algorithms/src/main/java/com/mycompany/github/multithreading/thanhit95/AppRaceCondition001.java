package com.mycompany.github.multithreading.thanhit95;

import java.util.List;
import java.util.stream.IntStream;

public class AppRaceCondition001 {
    public static void main(String[] args) {
        final int NUM_THREADS = 4;

        List<Thread> lstTh = IntStream.range(0, NUM_THREADS)
                .mapToObj(i -> new Thread(() -> {
                    try {Thread.sleep(1000);} catch(InterruptedException e) {}
                    System.out.print(i);
                }))
                .toList();
        lstTh.forEach(Thread::start);
    }
}
