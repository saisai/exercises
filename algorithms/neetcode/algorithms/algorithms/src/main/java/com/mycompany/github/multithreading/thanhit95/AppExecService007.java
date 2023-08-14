package com.mycompany.github.multithreading.thanhit95;

import java.util.concurrent.*;

public class AppExecService007 {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        // Old Syntax
//        Callable<Integer> callable = new Callable<Integer>() {
//            @Override
//            public Integer call() throws Exception {
//                return getSquared(7);
//            }
//        };

        Callable<Integer> callable = () -> getSquared(7);

        Future<Integer> task = executorService.submit(callable);
        executorService.shutdown();

        System.out.println("Calculating...");
        Integer result = task.get();
        System.out.println(result);
    }

    private static int getSquared(int x) {
        // Calculating in three seconds...
        try {
            Thread.sleep(3000);
        } catch(InterruptedException e) {
            e.printStackTrace();
        }

        return x * x;
    }
}
