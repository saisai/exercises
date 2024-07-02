package org.example.digitaloceancom.javahashmap;

import java.util.*;

public class HashMapEntrySetExample {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("1", "1");
        map.put("2", null);
        map.put(null, "100");

        Set<Map.Entry<String, String>> entrySet = map.entrySet();
        Iterator<Map.Entry<String, String>> iterator = entrySet.iterator();
        Map.Entry<String, String> next = null;

        System.out.println("map before processing = " + map);

        System.out.println("map before processing = "+map);
        System.out.println("entrySet before processing = "+entrySet);
        while(iterator.hasNext()) {
            next = iterator.next();
            System.out.println("Processing on: " + next.getValue());
            if(next.getValue() == null) iterator.remove();
        }

        System.out.println("map after processing = "+map);
        System.out.println("entrySet after processing = "+entrySet);

        Map.Entry<String, String> simpleEntry = new AbstractMap.SimpleEntry<String, String>("1","1");
        entrySet.remove(simpleEntry);
        System.out.println("map after removing Entry = "+map);
        System.out.println("entrySet after removing Entry = "+entrySet);

    }
}
