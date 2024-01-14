package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Array;

public class ArrayReflectionExample {
    public static void main(String[] args) {
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Get the length of the array using reflection
        int length = Array.getLength(numbers);
        System.out.println("Array length: " + length);

        // Get and print each element of the array using reflection
        for (int i = 0; i < length; i++) {
            int element = (int) Array.get(numbers, i);
            System.out.println("Element at index " + i + ": " + element);
        }
    }
}
