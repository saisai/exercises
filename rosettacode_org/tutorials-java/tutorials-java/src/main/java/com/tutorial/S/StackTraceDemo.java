package com.tutorial.S;

class StackTracer {
    public static void printStackTrace() {
        StackTraceElement[] elmes = Thread.currentThread().getStackTrace();;

        System.out.println("Stack trace:");
        for(int i = elmes.length-1, j = 2; i >= 3; i--, j+=2) {
            System.out.printf("%" + j + "s%s.%s%n", "", elmes[i].getClassName(), elmes[i].getMethodName());
        }
    }
}
public class StackTraceDemo {
    static void inner() {
        StackTracer.printStackTrace();
    }
    static void middle() {
        inner();
    }
    static void outer() {
        middle();
    }
    public static void main(String[] args) {
        outer();
    }
}
