package com.zetcode.app;

import java.util.function.Consumer;

public class DoubleColonOperator {

    private static void greet(String msg) {
        System.out.println(msg);
    }

    public static void main(String[] args) {
        Consumer<String> f= DoubleColonOperator::greet;
        f.accept("Hello there");
    }
}
