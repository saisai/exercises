package com.zetcode.app.interfacetutorial;

interface IInfo {
    void doInform();
}

class Some implements IInfo {
    @Override
    public  void doInform() {
        System.out.println("This is Some class");
    }
}

public class SimpleInterface {
    public static void main(String[] args) {
        Some sm = new Some();
        sm.doInform();
    }
}
