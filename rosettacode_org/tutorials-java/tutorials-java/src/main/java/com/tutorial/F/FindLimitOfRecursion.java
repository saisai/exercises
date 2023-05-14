package com.tutorial.F;

public class FindLimitOfRecursion {
    private static void recurse(int i) {
        try {
            recurse(i + 1);
        } catch(StackOverflowError e) {
            System.out.println("Recursion depth on this system is " + i + ".");
        }
    }

    public static void main(String[] args) {
        recurse(0);
    }
}
