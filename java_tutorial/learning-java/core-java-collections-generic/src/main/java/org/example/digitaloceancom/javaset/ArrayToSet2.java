package org.example.digitaloceancom.javaset;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ArrayToSet2 {
    public static void main(String[] args) {
        String[] vowels = {"a","e","i","o","u"};

        Set<String> vowelsSet = new HashSet<>();
        Collections.addAll(vowelsSet, vowels);
        System.out.println(vowelsSet);

        /**
         * Unlike List, Set is NOt backed by array,
         * so we can do structural modification without any issues.
         */
        vowelsSet.remove("e");
        System.out.println(vowelsSet);
        vowelsSet.clear();
        System.out.println(vowelsSet);
    }
}
