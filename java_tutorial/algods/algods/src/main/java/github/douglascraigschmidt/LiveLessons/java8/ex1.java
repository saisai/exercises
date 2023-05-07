package github.douglascraigschmidt.LiveLessons.java8;

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
                    System.out.println(string + (mRes += n)));
        }

        /**
         * The constructor creates/starts/runs a thread closure.
         */
        ClosureExample() throws InterruptedException {
            // Create a thred closure.
            Thread t = makeThreadClosure("result = ", 10);
            // start the thread
            t.start();
            // join when the thread is finished.
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

    /**
     * This {@link Supplier} makes a copy of an array.
     */
    private static final Supplier<String[]> sArrayCopy = () -> Arrays.copyOf(sNameArray, sNameArray.length);

    /**
     * Show how to sort using an anonymous inner class.
     */
    private static void showInnerClass(String... nameArray) {
        System.out.println("showInnerClass()");
        // sort using an anonymous inner class
        Arrays.sort(nameArray, new Comparator<String>() {
            @Override
            public int compare(String s, String t) {
                return s.toLowerCase().compareTo(t.toLowerCase());
            }
        });

        System.out.println(Arrays.asList(nameArray));
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
        System.out.println(Arrays.asList(nameArray));
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
        Arrays.asList(nameArray).forEach(System.out::print);
    }

    /**
     * This method provides the entry point into this test program.
     */
    public static void main(String[] args) throws InterruptedException {
        // first demostratres the closure example.
        new ClosureExample();
        // Next demonstrate various techniques for sorting/printing an array.
        System.out.println("Original array:\n"
                + Arrays.asList(sNameArray));
        showInnerClass(sArrayCopy.get());
        showLambdaExpression(sArrayCopy.get());
        showMethodReference1(sArrayCopy.get());
        showMethodReference2(sArrayCopy.get());

    }


}

// https://github.com/douglascraigschmidt/LiveLessons/blob/master/Java8/ex1/src/main/java/ex1.java
