package com.mycompany.github.multithreading.thanhit95;

import java.util.List;
import java.util.concurrent.*;
import java.util.stream.IntStream;

public class AppExecService009 {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        final int NUM_THREADS = 2;
        final int NUM_TASKS = 5;

        ExecutorService executorService = Executors.newFixedThreadPool(NUM_THREADS);

        List<Callable<String>> todo = IntStream.range(0, NUM_TASKS)
                .mapToObj(i -> (Callable<String>)() -> doTask(i))
                .toList();

        System.out.println("Begin to submit all tasks");

        /*
         * invokeAll() will not return until all the tasks are completed
         * (i.e., all the Futures in your answer collection will report isDone() if asked)
         */
        List<Future<String>> lstTask = executorService.invokeAll(todo);

        System.out.println("All tasks are completed");

        executorService.shutdown();

        for(Future<String> task : lstTask) {
            System.out.println(task.get());
        }

    }

    private static String doTask(int number) {
        try { Thread.sleep(3000); } catch (InterruptedException e) {}
        System.out.println("Finished " + number);
        return number + " ok";
    }
}
