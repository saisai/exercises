package com.zetcode.app.string;

import java.text.BreakIterator;

public class StringLength {
    public static void main(String[] args) {

        String text1 = "falcon";
        int n1 = text1.length();

        System.out.printf("%s has %d characters %n", text1, n1);

        System.out.println("----------------------------");

        String text2 = "вишня";
        int n2 = text2.length();
        System.out.printf("%s has %d characters%n", text2, n2);

        System.out.println("----------------------------");

        String text3 = "🐺🦊🦝";
        int n3 = text3.length();
        System.out.printf("%s has %d characters%n", text3, n3);

        int n3_ = graphemeLength(text3);
        System.out.printf("%s has %d characters%n", text3, n3_);

        System.out.println("----------------------------");

        String text4 = "नमस्ते";

        int n4 = text4.length();
        System.out.printf("%s has %d characters%n", text4, n4);

        int n4_ = graphemeLength(text4);
        System.out.printf("%s has %d characters%n", text4, n4_);
    }

    public static int graphemeLength(String text) {
        BreakIterator it = BreakIterator.getCharacterInstance();
        it.setText(text);
        int count = 0;
        while(it.next() != BreakIterator.DONE) {
            count++;
        }
        return count;
    }
}
