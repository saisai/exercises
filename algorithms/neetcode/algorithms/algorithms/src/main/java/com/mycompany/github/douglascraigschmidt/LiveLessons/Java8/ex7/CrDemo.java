package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8.ex7;

public class CrDemo implements Runnable{

    String mString;

    CrDemo() {
        mString = "Hello";
    }

    public CrDemo(String s, Integer i, Long l) {
        mString = s + i + l;
    }

    @Override
    public void run() {
        System.out.println(mString);
    }
}
