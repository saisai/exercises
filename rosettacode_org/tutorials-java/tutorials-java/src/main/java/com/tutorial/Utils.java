package com.tutorial;

import java.util.Objects;

public class Utils {

     public String getFilename() {
        String filePath = Objects.requireNonNull(getClass().getClassLoader().getResource("foobar.txt")).getPath();
        System.out.println("file path " + filePath);
        return filePath;
    }

}
