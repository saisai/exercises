package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.List;

public class TraversingList {
    public static void main(String[] args) {
        List<String> martialArts = new ArrayList<>();

        martialArts.add("Silat");
        martialArts.add("Wing chun");
        martialArts.add("Karate");
        martialArts.add("Judo");
        martialArts.add("Aikido");

        for(int i = 0; i < martialArts.size(); i++) {
            System.out.printf("%s", martialArts.get(i));
        }

        System.out.print("\n");

        for (String e: martialArts) {

            System.out.printf("%s ", e);
        }
        System.out.print("\n");

        martialArts.forEach((e) -> System.out.printf("%s ", e));

        System.out.print("\n");
    }
}
