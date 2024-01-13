package xyz.demo2.basics.arrays.sort;

import java.util.Arrays;

public class ParallelSortExample {
    public static void main(String[] args) {
        int[] array = {5, 2, 8, 1, 9};

        System.out.println("Unsorted array: " + Arrays.toString(array));

        Arrays.parallelSort(array);

        System.out.println("Sorted array: " + Arrays.toString(array));
    }
}
