package com.tutorial.E;

public class EquilibriumIndex {

    public static void equlibruiumIndices(int[] sequence) {
        int totalSum = 0;
        for(int n : sequence) {
            totalSum += n;
        }

        // compare running sum to remaining sum to find equlibrium indices
        int runningSum = 0;
        for(int i = 0; i < sequence.length; i++) {
            int n = sequence[i];
            if(totalSum - runningSum - n == runningSum) {
                System.out.println(i);
            }
            runningSum += n;
        }
    }

    public static void main(String[] args) {
        int[] sequence = {-7, 1, 5, 2, -4, 3, 0};
        equlibruiumIndices(sequence);
    }
}
