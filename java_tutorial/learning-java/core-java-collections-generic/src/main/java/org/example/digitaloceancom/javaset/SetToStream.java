package org.example.digitaloceancom.javaset;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class SetToStream {
    public static void main(String[] args) {
        Set<String> vowelsSet = new HashSet<>();
        // add example
        vowelsSet.add("a");
        vowelsSet.add("e");
        vowelsSet.add("i");
        vowelsSet.add("o");
        vowelsSet.add("u");

        List<String> tt = vowelsSet.stream().collect(Collectors.toList());

        tt.forEach(System.out::println);

        //convert set to stream
        vowelsSet.forEach(System.out::println);
    }
}
