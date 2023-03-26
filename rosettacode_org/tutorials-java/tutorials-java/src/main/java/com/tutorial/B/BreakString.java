package com.tutorial.B;

import java.lang.reflect.Field;

public class BreakString {
    public static void main(String... args) throws Exception {
        Field f = String.class.getDeclaredField("value");
        f.setAccessible(true);
        f.set("cat", new char[]{'t', 'i','g','e','r'});
        System.out.println("cat");
        System.out.println("cat".length());
    }
}
