package com.mycompany.github.multithreading.thanhit95;

public class AppJoin001 {
    @SuppressWarnings("unused")
    private static void doHeavyTask() {
        // Do a heavy task, which takes a little time
        long sum = 0;
        for (int i = 0; i < 2000000000; ++i)
            sum += i;

        System.out.println("Done!");
    }

    public static void main(String[] args) throws InterruptedException {
        Thread th = new Thread(() -> doHeavyTask());
        th.start();
        th.join();

        System.out.println("Good bye");
    }
}
