package com.mycompany.github.multithreading.thanhit95;

public class AppJoin002 {
    public static void main(String[] args) {

        Thread thFoo = new Thread(() -> System.out.println("foo"));
        Thread thBar = new Thread(() -> System.out.println("bar"));

        thFoo.start();
        thBar.start();
    }

}
