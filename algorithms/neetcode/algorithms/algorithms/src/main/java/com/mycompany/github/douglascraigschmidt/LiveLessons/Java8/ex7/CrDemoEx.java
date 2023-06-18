package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8.ex7;

public class CrDemoEx implements Runnable {

    String mStirng;

    CrDemoEx() {
        mStirng = "Hello";
    }

    @Override
    public void run() {
        System.out.println(mStirng.toUpperCase());
    }
}
