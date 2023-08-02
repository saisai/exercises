/*
 * EXECUTOR SERVICES AND THREAD POOLS
 * Version C01: The executor service and Future objects - Getting started
 *
 * Future objects help you to programatically manage tasks, such as:
 * - Wait for a task to finish executing (and get result), with the "get" method.
 * - Cancel a task prematurely, with the "cancel" method.
 */


package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class AppExecService004 {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        Future<String> task = executorService.submit(() -> "lorem ipsum");

        executorService.shutdown();


        while(false == task.isDone()) {
            System.out.println("waiting..." );
        }

        String result = task.get();
        System.out.println(result);
    }
}
