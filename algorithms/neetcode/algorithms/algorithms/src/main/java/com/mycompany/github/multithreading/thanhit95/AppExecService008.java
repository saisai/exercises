package com.mycompany.github.multithreading.thanhit95;

import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.IntStream;

public class AppExecService008 {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        final int NUM_THREADS = 2;
        final int NUM_TASKS = 5;

        ExecutorService executorService = Executors.newFixedThreadPool(NUM_THREADS);

        System.out.println("Begin to submit all tasks");

        // lstTask is List< Future<Character> >

        List< Future<Character >> lstTask = IntStream.range(0, NUM_TASKS)
                .mapToObj(i -> executorService.submit(() -> (char)(i + 'A')))
                .toList();
        executorService.shutdown();
        for(Future<Character> task : lstTask) {
            System.out.println(task.get());
        }
    }
}
