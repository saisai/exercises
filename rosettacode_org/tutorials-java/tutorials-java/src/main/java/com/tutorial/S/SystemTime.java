package com.tutorial.S;

import java.util.Date;

public class SystemTime {
    public static void main(String... args) {
        System.out.format("%tc%n", System.currentTimeMillis());
        System.out.println();
        Date now = new Date();
        System.out.println(now);

        System.out.println(now.getTime());
    }
}
