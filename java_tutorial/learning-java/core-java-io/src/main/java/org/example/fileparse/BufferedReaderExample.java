package org.example.fileparse;

import org.checkerframework.checker.units.qual.A;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class BufferedReaderExample {
    protected static ArrayList<String> generateArrayListFromFile(String filename) {
        ArrayList<String> result = new ArrayList<>();

        try(BufferedReader br = new BufferedReader(new FileReader(filename))) {
            while(br.ready()) {
                result.add(br.readLine());
            }
            return result;
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
