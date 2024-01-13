package xyz.demo2.basics.arrays.sort;

import java.util.Arrays;

public class DoubleArraySortingExample {
    public static void main(String[] args) {
        double[] numbers = { 5.7, 2.3, 8.9, 1.2, 4.6 };

        // Sort the array in ascending order
        Arrays.sort(numbers);

        // Print the sorted array
        System.out.println("Sorted array in ascending order:");
        for (double num : numbers) {
            System.out.print(num + " ");
        }
    }
}
