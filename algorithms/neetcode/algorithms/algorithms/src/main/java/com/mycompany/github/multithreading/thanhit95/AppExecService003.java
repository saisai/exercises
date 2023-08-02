package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

public class AppExecService003 {
    public static void main(String[] args) throws InterruptedException {
        final int NUM_THREADS = 2;
        final int NUM_TASKS = 5;

        ExecutorService executorService = Executors.newFixedThreadPool(NUM_THREADS);

        IntStream.range(0, NUM_TASKS).forEach(i -> executorService.submit(() -> {
            char nameTask = (char) (i + 'A');
            System.out.println("Task %s is starting.".formatted(nameTask));
            try { Thread.sleep(3000); } catch (InterruptedException e) { }

            System.out.println("Task %c is completed".formatted(nameTask));
        }));

        executorService.shutdown();


        System.out.println("All tasks are submitted");

        executorService.awaitTermination(20, TimeUnit.SECONDS);

        System.out.println("All tasks are completed");
    }
}
