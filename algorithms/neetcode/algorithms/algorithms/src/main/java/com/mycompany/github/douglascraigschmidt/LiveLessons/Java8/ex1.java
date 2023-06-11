package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class ex1 {

    static class ClosureExample {
        private int mRes;
        Thread makeThreadClosure(String string, int n) {
            return new Thread(() ->
                    System.out.println(string + (mRes += n) ));
        }

        ClosureExample() throws InterruptedException {
            Thread t = makeThreadClosure("result =", 10);
            t.start();
            t.join();
        }
    }

    /**
     * The array to sort and print.
     */
    private static final String[] sNameArray = {
            "Barbara",
            "James",
            "Mary",
            "John",
            "Robert",
            "Michael",
            "Linda",
            "james",
            "mary"
    };

    private static final Supplier<String[]> sArrayCopy = () -> Arrays.copyOf(sNameArray, sNameArray.length);

    private static void showInnerClass(String[] nameArray) {
        System.out.println("showInnterClass()");

        // Sort using an anyonumous inner class
        Arrays.sort(nameArray, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.toLowerCase().compareTo(o2.toLowerCase());
            }
        });

        // Print out the sorted contents as an array.
        System.out.println(List.of(nameArray));
    }

    /**
     * Show how to sort using a lambda expression.
     */
    private static void showLambdaExpression(String[] nameArray) {
        System.out.println("showLambdaExpression()");

        // Sort using a lambda expression.
        Arrays.sort(nameArray,
                // Note type deduction here:
                (s, t) -> s.compareToIgnoreCase(t));

        // Print out the sorted contents as an array.
        System.out.println(List.of(nameArray));
    }

    /**
     * Show how to sort using a method reference.
     */
    private static void showMethodReference1(String[] nameArray) {
        System.out.println("showMethodReference1()");

        // Sort using a method reference.
        Arrays.sort(nameArray,
                String::compareToIgnoreCase);

        // Print out the sorted contents using the modern Java Stream
        // forEach() method.
        Stream.of(nameArray).forEach(System.out::print);
    }

    /**
     * Show how to sort using a method reference.
     */
    private static void showMethodReference2(String[] nameArray) {
        System.out.println("\nshowMethodReference2()");

        // Sort using a method reference.
        Arrays.sort(nameArray,
                String::compareToIgnoreCase);

        // Print out the sorted contents using the modern Java Iterable
        // forEach() method.
        List.of(nameArray).forEach(System.out::print);
    }

    public static void main(String[] args) throws InterruptedException {
        new ClosureExample();

        // Next demonstrate various techniques for sorting/printing an array.
        System.out.println("Original array:\n"
                + List.of(sNameArray));

        System.out.println(Arrays.stream(sArrayCopy.get()).toList());
        showInnerClass(sArrayCopy.get());
        showLambdaExpression(sArrayCopy.get());
        showMethodReference1(sArrayCopy.get());
        showMethodReference2(sArrayCopy.get());



    }
}
