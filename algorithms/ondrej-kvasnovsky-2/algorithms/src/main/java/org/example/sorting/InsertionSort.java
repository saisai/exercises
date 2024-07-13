package org.example.sorting;

import java.util.Arrays;

public class InsertionSort {
    public static void insertionSort(int[] array) {
        int j;
        for(int i = 1; i < array.length; i++) {
            j = i;
            while((j > 0) && (array[j] < array[j - 1])) {
                swap(array, j, j - 1);
                j = j - 1;
                System.out.println(Arrays.toString(array));
            }
        }
    }

    public static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) {
        int[] array = {5, 4, 3, 2, 1};
        insertionSort(array);
    }
}
