package com.mycompany.github.multithreading.thanhit95;

import java.time.Duration;
import java.time.Instant;

public class AppYield001 {
    private static void littleSleep(int ns) {
        Instant tpStart = Instant.now();
        Instant tpEnd = tpStart.plusNanos(ns);

        do {
            Thread.yield();
        } while(Instant.now().isBefore(tpEnd));
    }

    public static void main(String[] args) {
        Instant tpStartMeasure = Instant.now();

        littleSleep(130000);

        Duration timeElapsed = Duration.between(tpStartMeasure, Instant.now());
        System.out.println("Elapsed time: " + timeElapsed.toNanos() + " nanoseonds");
    }
}
