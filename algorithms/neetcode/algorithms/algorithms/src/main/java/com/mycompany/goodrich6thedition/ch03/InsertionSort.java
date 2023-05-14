package com.mycompany.goodrich6thedition.ch03;

import java.util.Arrays;

public class InsertionSort {
    public static void insertionSort(char[] data) {
        int n = data.length;
        for(int k = 1; k < n; k++) {
            char cur = data[k];
            int j = k;
            while(j > 0 && data[j - 1] > cur) {
                data[j] = data[j - 1];
                j--;
            }
            data[j] = cur;
        }
    }

    public static void main(String[] args) {
        char[] letters = {'B', 'C', 'D', 'A', 'E', 'H', 'G', 'F'};
        char[] others = new char[5];
        Arrays.fill(others, 'a');
        System.out.println(others);
        System.out.println(letters);
        insertionSort(letters);
        //Arrays.sort(letters);
        System.out.println(letters);
    }

}
