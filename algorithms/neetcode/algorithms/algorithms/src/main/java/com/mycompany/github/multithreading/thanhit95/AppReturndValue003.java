/*
 * GETTING RETURNED VALUES FROM THREADS
 */

package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class AppReturndValue003 {
    static class SimpleCalculator {
        private ExecutorService executor = Executors.newSingleThreadExecutor();

        public Future<Integer> calculate(Integer input) {
            return executor.submit(() -> {
                Thread.sleep(1000);
                return input * 2;
            });
        }

        public void shutdown() {
            executor.shutdown();
        }
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        SimpleCalculator cal = new SimpleCalculator();
        System.out.println("Begin calculating");

        Future futResult = cal.calculate(-9);

        //Integer result = (Integer) futResult.get();
        int result = (int) futResult.get();

        System.out.println("result " + result);

        cal.shutdown();
    }
}
