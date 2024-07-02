package org.example.digitaloceancom.javahashmap;

import java.util.HashMap;
import java.util.Map;

public class HashMapComputeExample {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("1", "1");
        map.put("2", "2");
        map.put(null, "10");
        map.put("10", null);

        System.out.println("map before compute = "+map);
        for (String key : map.keySet()) {
            map.compute(key, (k,v) -> {return k+v;});
        }
        map.compute("5", (k,v) -> {return k+v;}); //key not present, v = null
        System.out.println("map after compute = "+map);
    }
}
