package xyz.demo2.basics.arrays.sort;

import java.util.Arrays;

public class ByteArraySortingExample2 {
    public static void main(String[] args) {
        byte[] byteArray = {10, -5, 7, 0, 12, -3};

        // Sorting the byte array in ascending order
        Arrays.sort(byteArray);/*w   w   w  .  d  e  mo   2  s  .   c o  m */

        // Reversing the sorted byte array
        for (int i = 0; i < byteArray.length / 2; i++) {
            byte temp = byteArray[i];
            byteArray[i] = byteArray[byteArray.length - 1 - i];
            byteArray[byteArray.length - 1 - i] = temp;
        }

        // Displaying the sorted byte array in descending order
        for (byte b : byteArray) {
            System.out.print(b + " ");
        }
    }
}
