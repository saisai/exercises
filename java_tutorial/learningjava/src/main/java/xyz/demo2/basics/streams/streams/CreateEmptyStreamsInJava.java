package xyz.demo2.basics.streams.streams;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class CreateEmptyStreamsInJava {
    class MyClass {
        // Define your custom class here
    }
    public static void main(String[] args) {
        Stream<String> emptyStringStream = Stream.empty();

        long count = emptyStringStream.count();
        System.out.println("Cuont of emptyStringStream : " + count);

        IntStream emptyIntStream = IntStream.empty();

        // You can perform operations on the empty stream
        long count2 = emptyIntStream.count();
        System.out.println("Count of emptyIntStream: " + count2);

        Stream<MyClass> emptyCustomStream = Stream.empty();

        // You can perform operations on the empty stream
        long count3 = emptyCustomStream.count();
        System.out.println("Count of emptyCustomStream: " + count3);
    }
}
