package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class AppExecService002 {
    public static void main(String[] args) {
        final int NUM_THREADS = 2;
        final int NUM_TASKS = 5;

        ExecutorService executorService = Executors.newFixedThreadPool(NUM_THREADS);

        IntStream.range(0, NUM_TASKS).forEach(i -> executorService.submit(() -> {
            char nameTask = (char) (i + 'A');
            System.out.println("Task %c is staring.".formatted(nameTask));

            try { Thread.sleep(300); } catch (InterruptedException e) {}
            System.out.println("Task %c is complated.".formatted(nameTask));
        }));

        // shutdown() stops the ExecutorService from accepting new tasks
        // and closes down idle worker threads
        executorService.shutdown();
    }
}
