package com.tutorial.L;

import java.time.LocalDate;
import java.time.temporal.WeekFields;

public class LongYear {
    private static boolean longYear(int year) {
        return LocalDate.of(year, 12, 28).get(WeekFields.ISO.weekOfYear()) == 53;
    }

    public static void main(String... args) {
        System.out.printf("Long years this century:%n");
        for(int year = 2000; year < 2100; year++) {
            if(longYear(year)) {
                System.out.print(year + " ");
            }
        }
    }
}
