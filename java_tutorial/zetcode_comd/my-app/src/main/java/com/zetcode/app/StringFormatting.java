package com.zetcode.app;

public class StringFormatting {

    public static void main(String[] args) {

        int age = 34;
        String name = "William";

        String output = String.format("%s is %d year old.", name, age);
        System.out.println(output);

    }
}
