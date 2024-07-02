package org.example;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.stream.Stream;

public class StringToCharJava {
    public static void main(String[] args) {
        String str = "journaldev";

        //string to char array
        char[] chars = str.toCharArray();
        System.out.println(chars.length);
        System.out.println(Arrays.toString(chars));
        Stream<Character> ss = str.chars().mapToObj(c ->  (char) c);
        ss.forEach(s -> { System.out.print(s + " ");});

        //char at specific index
        char c = str.charAt(2);
        System.out.println(c);

        //Copy string characters to char array
        char[] chars1 = new char[7];
        str.getChars(0, 7, chars1, 0);
        System.out.println(chars1);
    }
}
