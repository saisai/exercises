package com.zetcode.app.method;

public class SumOfValues {
    public static int sum(int...vals) {

        int sum = 0;

        for (int val : vals) {
            sum += val;
        }

        return sum;
    }

    public static void main(String[] args) {

        int s1 = sum(1, 2, 3);
        int s2 = sum(1, 2, 3, 4, 5);
        int s3 = sum(1, 2, 3, 4, 5, 6, 7);

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
    }
}
