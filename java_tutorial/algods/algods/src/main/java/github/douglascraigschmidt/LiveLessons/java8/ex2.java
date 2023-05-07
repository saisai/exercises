package github.douglascraigschmidt.LiveLessons.java8;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

public class ex2 {
    public static void main(String[] args) {
        // A List containing odd and even numbers.
        List<Integer> list =
                // Create a mutable List.
                new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 4, 3, 2, 1));

        // Print the items in the List.
        System.out.println(list);

        // Create a Predicate lambda that returns true if a number is
        // even, else false.
        Predicate<Integer> isEven = i -> i % 2 == 0;

        // This lambda expression removes the even numbers from the
        // list.
        list.remove(isEven);

        // Print the items in the stream.
        System.out.println(list);
    }
}
