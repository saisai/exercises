package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class ex6 {
    public static void main(String[] args) {
        Map<String, String> beingMap = new HashMap<String, String>() {{
            put("Demon", "Naughty");
            put("Angel", "Nice");
            put("Wizard", "Wise");
        }};

        beingMap.forEach(ex6::printDisposition);

        String being = "Demigod";

        Optional<String> disposition =
                Optional.ofNullable(beingMap.get(being));

        printDisposition(being,
                disposition.orElseGet(() -> "unknown"));
    }

    private static void printDisposition(String being,
                                         String disposition) {
        System.out.println("disposition of "
                + being + " = "
                + disposition);
    }
}
