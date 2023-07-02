package com.mycompany.docsoraclecom.collections.streams;

import com.mycompany.docsoraclecom.collections.streams.entities.User;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Stream001 {
    public static void main(String[] args) {
        Collection<String> collection = Arrays.asList("a", "b", "c");
        Stream<String> streamOfCollection = collection.stream();
        System.out.println(streamOfCollection);

        int reducedTwoParams =
                IntStream.range(1, 4).reduce(10, (a, b) -> a + b);

        System.out.println(reducedTwoParams);
        System.out.println();

        int reducedParams = Stream.of(1, 2, 3)
                .reduce(10, (a, b) -> a + b, (a, b) -> {
                    System.out.println("combiner was called");
                    return a + b;
                });
        System.out.println(reducedParams);


        int reducedParallel = Arrays.asList(1, 2, 3).parallelStream()
                .reduce(10, (a, b) -> a + b, (a, b) -> {
                    System.out.println("combiner was called");
                    return a + b;
                });
        System.out.println(reducedParallel);

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        int result1 = numbers.stream().reduce(0, (subtotal, element) -> subtotal + element);
        System.out.println(result1);

        int result2 = numbers.stream().reduce(0, Integer::sum);
        System.out.println(result2);

        List<String> letters = Arrays.asList("a", "b", "c", "d", "e");
        String result3 = letters.stream().reduce("", (partialString, element) -> partialString + element);
        System.out.println(result3);

        String result4 = letters.stream().reduce("", String::concat);
        System.out.println(result4);

        String result5 = letters.stream().reduce("", (partialString, element) -> partialString.toUpperCase() + element.toUpperCase());
        System.out.println(result5);

        List<User> users = Arrays.asList(new User("John", 30), new User("Julie", 35));
        int result6 = users.stream().reduce(0, (partialAgeResult, user) -> partialAgeResult + user.getAge(), Integer::sum);
        System.out.println(result6);

        String result7 = letters.parallelStream().reduce("", String::concat);
        System.out.println(result7);

        int result8 = users.parallelStream().reduce(0, (partialAgeResult, user) -> partialAgeResult + user.getAge(), Integer::sum);
        System.out.println(result8);
    }
}


// https://www.baeldung.com/java-8-streams