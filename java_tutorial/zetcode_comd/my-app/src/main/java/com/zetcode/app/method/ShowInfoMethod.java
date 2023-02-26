package com.zetcode.app.method;

class Base {
    public void showInfo() {
        System.out.println("This is Base class");
    }
}

public class ShowInfoMethod {

    public static void main(String[] args) {
        Base bs = new Base();
        bs.showInfo();
    }
}
