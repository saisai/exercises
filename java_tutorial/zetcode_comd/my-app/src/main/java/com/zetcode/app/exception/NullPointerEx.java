package com.zetcode.app.exception;

import java.util.ArrayList;
import java.util.List;

public class NullPointerEx {

    public static void main(String[] args) {

        List<String> words = new ArrayList() {{
            add("sky");
            add("blue");
            add("cloud");
            add(null);
            add("ocean");
        }};

        words.forEach(word -> {
            System.out.printf("The %s word has %d letters%n", word, word.length());
        });
    }
}
