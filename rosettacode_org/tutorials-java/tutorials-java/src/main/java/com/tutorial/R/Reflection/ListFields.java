package com.tutorial.R.Reflection;

import java.io.File;
import java.lang.reflect.Field;

class Parent {

    public int idx = 100;
    public String hello = "hello";

    public String[] tesing = {"hello", "10"};
}

public class ListFields  extends Parent{

    public int examplePublicField = 42;
    private boolean examplePrivateField = true;

    public static void main(String... args) throws IllegalAccessException {
        ListFields obj = new ListFields();
        Class clazz = obj.getClass();

        System.out.printf("All public fields (including inheried):\n");
        for(Field f : clazz.getFields()) {
            System.out.println("test " + f.get(obj).getClass().toString());
            System.out.printf("%s\t%s\n", f, f.get(obj));
        }
        System.out.println();
        System.out.println("All declared fields (excluding inheried):");
        for(Field f : clazz.getDeclaredFields()) {
            System.out.printf("%s\t%s\n", f, f.get(obj));
        }
    }
}
