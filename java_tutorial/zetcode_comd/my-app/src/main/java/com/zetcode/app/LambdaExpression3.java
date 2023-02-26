package com.zetcode.app;

import java.util.function.Function;

public class LambdaExpression3 {

    public static void main(String[] args) {
        Function<Integer, Integer> square = (Integer x) -> x * x;
        System.out.println(square.apply(5));
    }
}
