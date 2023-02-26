package com.zetcode.app.method;

class Cat {}
class Dog {}
public class PassByValue {

    private static void tryChangeInteger(int x) {

        x = 15;
    }

    private static void tryChangeObject(Object o) {

        Dog d = new Dog();
        o = d;
    }

    public static void main(String[] args) {

        int n = 10;
        tryChangeInteger(n);
        System.out.println(n);

        Cat c = new Cat();
        tryChangeObject(c);
        System.out.println(c.getClass());
    }
}
