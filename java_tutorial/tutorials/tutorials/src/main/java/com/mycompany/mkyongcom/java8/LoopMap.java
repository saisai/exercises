package com.mycompany.mkyongcom.java8;

import sun.util.resources.cldr.zh.CalendarData_zh_Hans_HK;

import java.util.HashMap;
import java.util.Map;

public class LoopMap {

    public void loopMapClassic() {
        Map<String, Integer> map = new HashMap<>();
        map.put("A", 10);
        map.put("B", 20);
        map.put("C", 30);
        map.put("D", 40);
        map.put("E", 50);
        map.put("F", 60);

        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Key : " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }

    public static void loopMapJava8() {
        Map<String, Integer> map = new HashMap<>();
        map.put("A", 10);
        map.put("B", 20);
        map.put("C", 30);
        map.put("D", 40);
        map.put("E", 50);
        map.put("F", 60);

        // lambda
        map.forEach((k, v) -> System.out.println("Key : " + k + "Value : " + v));

        // ensure map is not null
        if (map != null) {
            map.forEach((k, v) -> System.out.println("Key : " + k + ", Value : " + v));
        }

        map.forEach(
                (k, v) -> {
                    // yes, we can put logic here
                    if(k != null) {
                        System.out.println("Key : " + k + ", Value :" + v);
                    }
                }
        );
    }
    public static void main(String[] args) {

        LoopMap loopMap = new LoopMap();
        loopMap.loopMapClassic();
        loopMap.loopMapJava8();

    }
}

// https://mkyong.com/java8/java-8-foreach-examples/
