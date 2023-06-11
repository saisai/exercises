package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;

import java.util.function.Function;

public class ex3 {

    static public class HtmlTagMaker {
        static String addLessThan(String text) {
            return "<" + text;
        }

        static String addGreaterThan(String text) {
            return text + ">";
        }
    }

    public static void main(String[] args) {
        Function<String, String> lessThan = HtmlTagMaker::addLessThan;;
        Function<String, String> tagger = lessThan.andThen(HtmlTagMaker::addGreaterThan);

        String html = tagger.apply("HTML")
                + tagger.apply("BODY")
                + tagger.apply("/BODY")
                + tagger.apply("/HTML");

        System.out.println(html);
    }
}
