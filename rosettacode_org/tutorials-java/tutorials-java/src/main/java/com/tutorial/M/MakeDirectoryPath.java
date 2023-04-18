package com.tutorial.M;

import java.io.File;

public class MakeDirectoryPath {
    public static void main(String[] args) {
        try{
            File f = new File("D:/parent/test");
            if(f.mkdirs())
                System.out.println("Path successfully created");
            System.out.println(f.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
