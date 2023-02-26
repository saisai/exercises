package com.zetcode.app;

public class ArraysEx {
    public static void main(String[] args) {
        int[] numbers = new int[5];

        numbers[0] = 3;
        numbers[1] = 2;
        numbers[2] = 1;
        numbers[3] = 5;
        numbers[4] = 6;

        int len = numbers.length;

        for(int i=0; i < len; i++) {
            System.out.println(numbers[i]);
        }
    }
}
