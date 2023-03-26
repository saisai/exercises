package com.tutorial.R;

import com.tutorial.Utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class ReadAFileCharacterByCharacter {

    public static void main(String... args) throws IOException {
        String fileName = new Utils().getFilename("unixdict.txt");
        FileReader reader = new FileReader(fileName);
        while(true) {
            int c = reader.read();
            if(c == -1) break;
            System.out.print(Character.toChars(c));
        }
    }
}
