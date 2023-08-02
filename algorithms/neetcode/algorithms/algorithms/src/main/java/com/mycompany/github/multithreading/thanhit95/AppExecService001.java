/*
 * EXECUTOR SERVICES AND THREAD POOLS
 * Version A: The executor service (of which thread pool) containing a single thread
 *
 * Note: The single thread executor is ideal for creating an event loop.
 */

package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AppExecService001 {
    public static void main(String[] args) {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        executorService.submit(() -> System.out.println("Hello world"));
        executorService.submit(() -> System.out.print("Hello Multithreading."));

        Runnable rnn = () -> System.out.print("Hello the Executor service");
        executorService.submit(rnn);

        executorService.shutdown();
    }
}
