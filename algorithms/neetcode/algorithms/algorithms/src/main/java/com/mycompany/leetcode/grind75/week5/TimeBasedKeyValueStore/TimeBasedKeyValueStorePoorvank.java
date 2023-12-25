package com.mycompany.leetcode.grind75.week5.TimeBasedKeyValueStore;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class TimeBasedKeyValueStorePoorvank {
    private Map<String, TreeMap<Integer, String>> map;

    public TimeBasedKeyValueStorePoorvank() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)) {
            map.put(key, new TreeMap<>());
        }
        map.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        TreeMap<Integer, String> treeMap = map.get(key);
        if(treeMap == null) {
            return "";
        }
        Integer floor = treeMap.floorKey(timestamp);
        if(floor == null) {
            return "";
        }
        return treeMap.get(floor);
    }

    public static void main(String[] args) {
        TimeBasedKeyValueStorePoorvank timeMap = new TimeBasedKeyValueStorePoorvank();
        timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
        System.out.println(timeMap.get("foo", 1)  );
        System.out.println(timeMap.get("foo", 3)  );
        timeMap.set("foo", "bar2", 4);
        System.out.println(timeMap.get("foo", 4)  );
        System.out.println(timeMap.get("foo", 5)  );
    }
}
