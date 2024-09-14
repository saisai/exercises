package org.example.sequences;

public class SequencesDemo {
    // without recursion
    private static int fib(int nth) {
        int index = nth - 2;
        int previous = 1;
        int current = 1;
        while(index > 0) {
            int sum = previous + current;
            previous = current;
            current = sum;
            System.out.println(sum);
            index--;
        }
        return current;
    }

    private static int fibRecursion(int nth) {
        if(nth == 0 || nth == 1) {
            return 1;
        }
        return fibRecursion(nth - 1) + fibRecursion(nth - 2);
    }

    public static void main(String[] args) {
        System.out.println("Fib: " + fib(1)); // 1
        System.out.println("Fib: " + fib(2)); // 1
        System.out.println("Fib: " + fib(3)); // 3
        System.out.println("Fib: " + fib(6)); // 8

        System.out.println("fibRecursion: " + fibRecursion(1)); // 1
        System.out.println("fibRecursion: " + fibRecursion(2)); // 1
        System.out.println("fibRecursion: " + fibRecursion(5)); // 3
        System.out.println("fibRecursion: " + fibRecursion(8)); // 8
    }
}

// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/sequences/fibonacci-sequence