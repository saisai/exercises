package com.mycompany.github.winterbe.java8tutorial.stream;

import java.util.Optional;

public class Optional1 {
    public static void main(String[] args) {
        Optional<String> optional = Optional.of("bam");

        optional.isPresent();
        optional.get();
        optional.orElse("fallback");
        optional.ifPresent((s) -> System.out.println(s.charAt(0)));
    }
}

 // https://github.com/winterbe/java8-tutorial/blob/master/src/com/winterbe/java8/samples/stream/Optional1.java
