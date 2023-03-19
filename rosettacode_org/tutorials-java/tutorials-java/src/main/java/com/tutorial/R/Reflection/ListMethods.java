package com.tutorial.R.Reflection;

import java.lang.reflect.Method;
import java.util.Arrays;

public class ListMethods {

    public int number;
    public String hello;

    public int examplePublicInstanceMethod(char c, double d) {
        return 42;
    }

    private boolean examplePrivateInstanceMethod(String s) {
        return true;
    }

    public static void main(String... args) {
        Class clazz = ListMethods.class;

        System.out.println("All public methods (including inerited):");

        System.out.println(clazz.toString());
        System.out.println("Fields of myclass : " +
                Arrays.toString(clazz.getFields()));

        for(Method m : clazz.getMethods()) {
            System.out.println(m);
        }

        System.out.println();
        System.out.println("All declared methods (excluding inherired):");
        for(Method m : clazz.getDeclaredMethods()) {
            System.out.println(m);
        }
    }
}
