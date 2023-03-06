package com.tutorial.L;

import java.time.Year;

public class IsLeap {

    public static void main(String... args) {
        int[] years = {2000, 2001, 2002, 2003};

        for(int year : years) {
            System.out.println("Year " + year + " is " + Year.isLeap(year));
        }

        System.out.println(Year.isLeap(2004));
        System.out.println(Year.now());
    }
}
