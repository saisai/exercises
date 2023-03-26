package com.tutorial.Two;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import java.util.Stack;

public class Game24 {

    static Random r = new Random();
    static int[] randomDigits() {
        int[] result = new int[4];
        for(int i = 0; i < 4; i++) {
            result[i] = r.nextInt(9) + 1;
        }
        return result;
    }

    static long tallyDigits(int[] a) {
        long total = 0;
        for(int i = 0; i < 4; i++)
            total += ( 1 << (a[i] * 5));
        return total;
    }

    static float applyOrder(float a, float b, char c) {
        switch (c) {
            case '+':
                return a + b;
            case '-':
                return b - a;
            case '*':
                return a * b;
            case '/':
                return b / a;
            default:
                return Float.NaN;
        }
    }

    public static void main(String... args) {
        int[] digits = randomDigits();
        Scanner in = new Scanner(System.in);

        System.out.print("Make 24 using these digits: ");
        System.out.println(Arrays.toString(digits));
        System.out.print("> ");

        Stack<Float> s = new Stack<Float>();
        long total = 0;
        for(char c : in.nextLine().toCharArray()) {
            if('0' <= c && c <= '9') {
                int d = c - '0';
                total += ( 1 << (d * 5));
                s.push((float) d);
            } else if("+/-*".indexOf(c) != -1) {
                s.push(applyOrder(s.pop(), s.pop(), c));
            }
        }

        if (tallyDigits(digits) != total)
            System.out.print("Not the same digits. ");
        else if (Math.abs(24 - s.peek()) < 0.001F) {
            System.out.println("Correct");
        } else
            System.out.print("Not Correct.");
    }
}
