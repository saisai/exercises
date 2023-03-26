package com.tutorial;

import java.util.Objects;

public class Utils {

     public String getFilename(String fileName) {
        String filePath = Objects.requireNonNull(getClass().getClassLoader().getResource(fileName)).getPath();
        System.out.println("file path " + fileName);
        return filePath;
    }

}
