package com.zetcode.app;

interface GreetingService {
    void greet(String message);
}
public class LambdaExpression2 {

    public static void main(String[] args) {
        GreetingService gs = (String msg) -> {
            System.out.println(msg);
        };

        gs.greet("Good night");
        gs.greet("Hello there");
    }
}
