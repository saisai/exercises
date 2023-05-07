package com.tutorial.E;

public class EnvironmentVariables {
    public static void main(String[] args) {
        System.out.println(System.getenv("HOME"));

        System.getenv().forEach(
                (k, v) -> System.out.printf("Key %s : Value %s%n", k, v)
        );

    }
}
