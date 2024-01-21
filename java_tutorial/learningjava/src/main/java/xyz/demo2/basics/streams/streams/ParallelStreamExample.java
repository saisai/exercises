package xyz.demo2.basics.streams.streams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class ParallelStreamExample {
    public static void main(String[] args) {
//        List<Integer> integerList = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
//        IntStream parallelStream = (IntStream) integerList.parallelStream();
        Integer[] intArray = {1, 2, 3, 4, 5, 6, 7, 8 };
        List<Integer> listOfIntegers =
                new ArrayList<>(Arrays.asList(intArray));



        listOfIntegers.parallelStream().forEach(value -> { System.out.println("Value : " + value);});

    }
}
