package org.example.digitaloceancom;

import java.io.File;
import java.io.IOException;

public class CreateNewFile {
    public static void main(String[] args) throws IOException {
        String fileSeparator = System.getProperty("file.separator");
        System.out.println(fileSeparator);
        //absolute file name with path
        String absoluteFilePath = "D:\\tmp"+fileSeparator+"zfile.txt";
        File file = new File(absoluteFilePath);
        if(file.createNewFile()){
            System.out.println(absoluteFilePath+" File Created");
        }else System.out.println("File "+absoluteFilePath+" already exists");

        //file name only
        file = new File("file.txt");
        if(file.createNewFile()){
            System.out.println("file.txt File Created in Project root directory");
        }else System.out.println("File file.txt already exists in the project root directory");

    }
}
