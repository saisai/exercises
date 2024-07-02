package org.example.digitaloceancom.javahashmap;

import java.util.HashMap;
import java.util.Map;

public class HashMapMergeExample {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("1", "1");
        map.put("2", "2");
        map.put(null, "10");
        map.put("10", null);

        for (Map.Entry<String, String> entry : map.entrySet()) {
            String key = entry.getKey();
            String value = entry.getValue();
            //merge throws NullPointerException if key or value is null
            if(key != null && value != null)
                map.merge(entry.getKey(), entry.getValue(),
                        (k, v) -> {return k + v;});
        }
        System.out.println(map);

        map.merge("5", "5", (k, v) -> {return k + v;}); // key not present
        System.out.println(map);

        map.merge("1", "1", (k, v) -> {return null;}); // method return null, so remove
        System.out.println(map);
    }
}
