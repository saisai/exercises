package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class ex4 {

    public static void main(String[] args) {
        Map<String, Integer> stoogeMap =
                new ConcurrentHashMap<String, Integer>() {{
                    put("Larry", 100);
                    put("Curly", 90);
                    put("Moe", 110);
                }};

        System.out.println(stoogeMap);

        for(Map.Entry<String, Integer> entry : stoogeMap.entrySet())
            entry.setValue(entry.getValue() - 50);

        System.out.println(stoogeMap);

        stoogeMap.replaceAll((k, v) -> v - 50);

        System.out.println(stoogeMap);
    }
}
