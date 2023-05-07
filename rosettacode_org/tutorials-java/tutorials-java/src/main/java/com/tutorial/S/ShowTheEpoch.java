package com.tutorial.S;

import org.omg.CORBA.TIMEOUT;

import java.text.DateFormat;
import java.util.Date;
import java.util.TimeZone;

public class ShowTheEpoch {
    public static void main(String[] args) {
        Date date = new Date(0);
        DateFormat dateFormat = DateFormat.getDateTimeInstance();
        dateFormat.setTimeZone(TimeZone.getTimeZone("UTC"));
        System.out.println(dateFormat.format(date));
    }
}
