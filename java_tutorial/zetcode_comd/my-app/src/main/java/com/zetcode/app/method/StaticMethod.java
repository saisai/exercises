package com.zetcode.app.method;

class Basic {

    static int id = 2321;

    public static void showInfo() {

        System.out.println("This is Basic class");
        System.out.format("The Id is: %d%n", id);
    }
}
public class StaticMethod {
    public static void main(String[] args) {

        Basic.showInfo();
    }
}
