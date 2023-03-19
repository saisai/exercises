package api.java.util.arrays;

import java.util.Arrays;

public class Arrays001 {
    public static void main(String... args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };

        int sum = 0;
        for(int i = 0 ; i < arr.length; i++) {
            sum += arr[i];
        }

        System.out.println("Average using iteration :" +
                (sum / arr.length));

        // Let's try the declarative style now
        sum = Arrays.stream(arr) // step 1
                .sum();         // step 2
        System.out.println("Average using streams : " +
                (sum / arr.length));

        // forEach()
        // It iterates through the entire streams
        System.out.println("Printing array elements : ");
        Arrays.stream(arr)
                .forEach(e -> System.out.print(e + " "));
    }
}
