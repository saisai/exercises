package com.tutorial.I;

import java.util.function.IntPredicate;
import java.util.stream.IntStream;

public class IdiomaticallyDetermineAllTheCharactersThatCanBeUsedForSymbols {
    static void print(String msg, int start, int end, int limit, IntPredicate p, String fmt) {
        System.out.print(msg);

        IntStream.rangeClosed(start, end)
                .filter(p)
                .limit(limit)
                .forEach(cp -> System.out.printf(fmt, cp));
        System.out.println("...");
    }

    public static void main(String[] args) {
        print("Java Identifier start:     ", 0, 0x10FFFF, 72,
                Character::isJavaIdentifierStart, "%c");

        print("Java Identifier part:      ", 0, 0x10FFFF, 25,
                Character::isJavaIdentifierPart, "[%d]");

        print("Identifier ignorable:      ", 0, 0x10FFFF, 25,
                Character::isIdentifierIgnorable, "[%d]");

        print("Unicode Identifier start:  ", 0, 0x10FFFF, 72,
                Character::isUnicodeIdentifierStart, "%c");

        print("Unicode Identifier part :  ", 0, 0x10FFFF, 25,
                Character::isUnicodeIdentifierPart, "[%d]");


    }
}
