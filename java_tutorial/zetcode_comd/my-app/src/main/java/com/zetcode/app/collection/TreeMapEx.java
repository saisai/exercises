package com.zetcode.app.collection;

import java.util.TreeMap;

public class TreeMapEx {

    public static void main(String[] args) {

        TreeMap<String, String> domains = new TreeMap<>();

        domains.put("de", "Germany");
        domains.put("sk", "Slovakia");
        domains.put("us", "United States");
        domains.put("ru", "Russia");
        domains.put("hu", "Hungary");
        domains.put("pl", "Poland");

        System.out.println(domains);
        System.out.println(domains.descendingMap());
    }
}
