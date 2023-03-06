package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayListSimpleEx {

    public static void main (String[] args) {

        List<String> distros = new ArrayList<>();
        distros.add("Manjaro");
        distros.add("Xubuntu");
        distros.add("Fedora");
        distros.add("elementary");

        for(String distro: distros) {
            System.out.println(distro);
        }

        List<String> capitals = Arrays.asList("Prague", "Bratiislava", "Warsaw", "Budapest",
                                "Washington");
        for(String capital : capitals) {
            System.out.println(capital);
        }


    }
}
