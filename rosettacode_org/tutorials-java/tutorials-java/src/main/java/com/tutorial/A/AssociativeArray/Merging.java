package com.tutorial.A.AssociativeArray;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Objects;

public class Merging {
    public static void main(String[] args) {
        Map<String, Object> base = new HashMap<>();
        base.put("name", "Rocket Skates");
        base.put("price", 12.75);
        base.put("color", "yellow");

        Map<String, Object> update = new HashMap<>();
        update.put("price", 15.25);
        update.put("color", "red");
        update.put("year", 1974);

        Map<String, Object> result = new HashMap<>(base);
        result.putAll(update);

        System.out.println(result);

        for(Map.Entry<String, Object> entry : result.entrySet()) {
            System.out.println("Key =" + entry.getKey() + ", Value =" + entry.getValue());
        }

        for(String name : result.keySet()) {
            System.out.println("Key : " + name);
        }

        for(Object obj : result.values()) {
            System.out.println("value : " + obj);
        }

        System.out.println();

        // Using iterators
        Iterator<Map.Entry<String, Object>> itr = result.entrySet().iterator();

        while(itr.hasNext()) {
            Map.Entry<String, Object> entry = itr.next();
            System.out.println("Key = " + entry.getKey() +
                    ", Value = " + entry.getValue());
        }

        System.out.println();
        // forEach(action) method to iterate map
        result.forEach((k, v) -> System.out.println("key =" + k + ", Value =" + v));
        System.out.println();

        // looping over keys
        for(String name : result.keySet()) {
            Object obj = result.get(name);
            System.out.println("key =" + name + ", Value = " + obj);
        }
        System.out.println();
        // iterating over keys:
        result.keySet().forEach(k -> System.out.printf("key = %s%n", k));

        System.out.println();
        // iterating over values:
        result.values().forEach(v -> System.out.printf("value = %s%n", v));

        System.out.println();


    }
}
