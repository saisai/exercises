package com.mycompany.github.multithreading.thanhit95;

import java.util.stream.IntStream;

public class AppListThread003 {
    public static void main(String[] args) {
        IntStream.range(0, 5).forEach(i -> new Thread(() -> {
            try {Thread.sleep(500); }
            catch(InterruptedException e) {}

            System.out.print(" " + i);
        }).start());
    }
}
