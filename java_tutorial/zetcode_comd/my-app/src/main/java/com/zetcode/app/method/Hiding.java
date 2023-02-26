package com.zetcode.app.method;

class BaseOne {

    public static void showInfo() {

        System.out.println("This is Base class");
    }
}

class Derived extends BaseOne {

    public static void showInfo() {

        System.out.println("This is Derived class");
    }
}
public class Hiding {
    public static void main(String[] args) {

        BaseOne.showInfo();
        Derived.showInfo();
    }
}
