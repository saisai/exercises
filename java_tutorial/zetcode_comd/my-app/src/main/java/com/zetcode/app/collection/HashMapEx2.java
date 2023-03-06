package com.zetcode.app.collection;

import java.util.HashMap;
import java.util.Map;

class Colour {

    private String name;
    private String code;

    public Colour(String name, String code) {
        this.name = name;
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}

public class HashMapEx2 {
    public static void main(String[] args) {
        Map<Integer, Colour> cols = new HashMap<>();

        cols.put(1, new Colour("AliceBlue", "#f0f8ff"));
        cols.put(2, new Colour("GreenYellow", "#adff2f"));
        cols.put(3, new Colour("IndianRed", "#cd5c5c"));
        cols.put(4, new Colour("khaki", "#f0e68c"));

        System.out.printf("The size of the map is %d%n", cols.size());

        int key = 4;

        if (cols.containsKey(key)) {

            System.out.printf("The map contains key %d%n", key);
        }

        cols.remove(1);

        System.out.printf("The size of the map is %d%n", cols.size());

        cols.replace(3, new Colour("VioletRed", "#d02090"));

        Colour col = cols.get(3);

        System.out.printf("Colour name:%s colour code:%s %n",
                col.getName(), col.getCode());
    }
}
