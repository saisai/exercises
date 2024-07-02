package org.example;

import java.util.Map;

public class Main {

    public void hello(int one, int two) {
        if(one > two) {
            return;
        }

        hello(one + 1, two);
    }


    public static void main(String[] args) {

        System.out.println("Hello world!");
        Main m = new Main();
        m.hello(1, 3);
    }
}