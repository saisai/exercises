package xyz.demo2.basics.arrays.sort;

import java.util.Arrays;

public class ByteArraySortingExample {
    public static void main(String[] args) {
        byte[] byteArray = {10, -5, 7, 0, 12, -3};

        // Sorting the byte array
        Arrays.sort(byteArray);

        // Displaying the sorted byte array
        for (byte b : byteArray) {
            System.out.print(b + " ");
        }
    }
}
