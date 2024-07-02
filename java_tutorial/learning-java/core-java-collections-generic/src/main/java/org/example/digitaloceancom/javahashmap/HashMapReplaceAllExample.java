package org.example.digitaloceancom.javahashmap;

import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;

public class HashMapReplaceAllExample {

    static class MyBiFunction implements BiFunction<String, String, String> {

        @Override
        public String apply(String t, String u) {
            if (t != null)
                return t + u;
            else
                return u;
        }

    }
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("1", "1");
        map.put("2", "2");
        map.put(null, "100");

        System.out.println("map before replaceAll = " + map);
        BiFunction<String, String, String> function = new MyBiFunction();
        map.replaceAll(function);
        System.out.println("map after replaceAll = " + map);

        // replaceAll using lambda expressions
        map.replaceAll((k, v) -> {
            if (k != null) return k + v;
            else return v;});
        System.out.println("map after replaceAll lambda expression = " + map);
    }
}
