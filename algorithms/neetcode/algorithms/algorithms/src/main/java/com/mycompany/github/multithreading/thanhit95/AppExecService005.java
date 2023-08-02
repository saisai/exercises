/*
 * EXECUTOR SERVICES AND THREAD POOLS
 * Version C02: The executor service and Future objects - Getting started
 */

package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class AppExecService005 {

    private static int getSquared(int x) {
        return x * x;
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        Future<Integer> task = executorService.submit(() -> getSquared(7));

        executorService.shutdown();

        while(false == task.isDone()) {
            // waiting...
        }

        Integer result = task.get();
        System.out.println(result);
    }
}
