package com.tutorial.F;

import java.io.File;

public class FileSize {

    static File getCwd() {
        return new File("").getAbsoluteFile();
    }
    public static void main(String[] args) {
        System.out.println(getCwd() + "\\pom.xml");
        System.out.println("input.txt : " + new File(getCwd() + "\\pom.xml").length() + " bytes");
    }
}
