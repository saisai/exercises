package com.zetcode.app;

public class Enumerations {

    enum Days {
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY
    }

    public  static  void main(String[] args) {
        Days day = Days.MONDAY;

        if (day == Days.MONDAY) {

            System.out.println("It is Monday");
        }

        System.out.println(day);

        for(Days d: Days.values()) {
            System.out.println(d);
        }
    }
}
