package com.tutorial.R;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class ReadEntireFile2 {
    public static List<String> readAllLines(String fileName) throws IOException {
        Path file = Paths.get(fileName);
        return Files.readAllLines(file, Charset.defaultCharset());
    }


    public static byte[] readAllBytes(String filename) throws IOException {
        Path file = Paths.get(filename);
        return Files.readAllBytes(file);
    }

    public static void main(String... args) throws IOException {
        File file = new File("src/main/resources/unixdict.txt");
        System.out.println("exists " + file.exists());
        String absolutePath = file.getAbsolutePath();
        System.out.println(absolutePath);
        List<String> result = readAllLines(absolutePath);

//        for(String r : result) {
//            System.out.println(r);
//        }

        byte[] byteResults = readAllBytes(absolutePath);

        String str = new String(byteResults, StandardCharsets.UTF_8);

        // https://stackoverflow.com/questions/1536054/how-to-convert-byte-array-to-string-and-vice-versa

       System.out.println(str);

    }
}
