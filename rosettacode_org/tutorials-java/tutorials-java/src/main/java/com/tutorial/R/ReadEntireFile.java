package com.tutorial.R;

import com.tutorial.Utils;

import java.io.FileReader;
import java.io.IOException;

public class ReadEntireFile {

    private static String readEntireFile(String fileName) throws IOException {
        FileReader in = new FileReader(fileName);
        StringBuffer contents = new StringBuffer();
        char[] buffer = new char[4098];
        int read = 0;
        do {
            contents.append(buffer, 0, read);
            read = in.read(buffer);
        } while (read >= 0);
        in.close();
        return contents.toString();
    }
    public static void main(String... args) throws IOException {

        String fileContents = readEntireFile(new Utils().getFilename("unixdict.txt"));
        System.out.println(fileContents);

    }
}
