package com.tutorial.C;

public class CharacterCodes {
    public static void main(String[] args) {
        System.out.println((int)'a');
        System.out.println((int)'b');

        char[] alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p'};

        for(int i = 0; i < alpha.length; i++) {
            System.out.println((int)alpha[i]);
        }

        for(int j = 97; j < 255; j++) {
            System.out.println((char)j);
        }
    }
}
