package com.zetcode.app.statickeyword;

public class JavaStaticNestedClass {

    private static int x = 5;

    static class Nested {
        @Override
        public String toString() {
            return "This is a static nested class; x:" + x;
        }
    }

    public static void main(String[] args) {
        JavaStaticNestedClass.Nested sn = new JavaStaticNestedClass.Nested();
        System.out.println(sn);
    }
}
