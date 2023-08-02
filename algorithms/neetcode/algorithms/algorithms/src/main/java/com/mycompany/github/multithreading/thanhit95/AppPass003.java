package com.mycompany.github.multithreading.thanhit95;

public class AppPass003 {
    public static void main(String[] args) {
        final int COUNT = 10;
        new Thread(() -> {
            for(int i = 1; i <= COUNT; ++i)
                System.out.println("value: " + i);
        }).start();
    }
}
