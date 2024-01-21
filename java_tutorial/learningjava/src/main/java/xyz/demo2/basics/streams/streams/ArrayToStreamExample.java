package xyz.demo2.basics.streams.streams;

import java.util.Arrays;
import java.util.stream.Stream;

public class ArrayToStreamExample {
    public static void main(String[] args) {
        Integer[] numbers = {1, 2, 3, 4, 5};
        Stream<Integer> stream = Arrays.stream(numbers);
        stream
                .filter(n -> n  % 2 == 0)
                .map( n -> n * 2)
                .forEach(System.out::println);


    }
}
