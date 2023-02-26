package com.zetcode.app.string;

public class Splitting {

    public static void main(String[] args) {
        String s = "Today is a beautiful day.";

        String[] words = s.split(" ");

        for(String word : words) {
            System.out.println(word);
        }
    }
}
