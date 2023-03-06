package com.zetcode.app.statickeyword;

public class JavaStaticBlock {

    private static int i;
    private static String name;

    static {

        System.out.println("Class initializer called");
        i = 6;
        name = "Jhon Terry";
    }

    public static void main(String[] args) {

        System.out.format("%d %s \n",i, name);
    }
}
