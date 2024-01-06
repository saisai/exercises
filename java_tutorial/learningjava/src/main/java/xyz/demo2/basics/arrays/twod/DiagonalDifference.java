package xyz.demo2.basics.arrays.twod;

public class DiagonalDifference {
    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        int diagonal1Sum = 0;
        int diagonal2Sum = 0;

        int n = matrix.length; // Assuming it's a square matrix

        for (int i = 0; i < n; i++) {
            diagonal1Sum += matrix[i][i]; // Main diagonal
            diagonal2Sum += matrix[i][n - 1 - i]; // Secondary diagonal
        }

        int difference = Math.abs(diagonal1Sum - diagonal2Sum);

        System.out.println("Diagonal Difference: " + difference);
    }
}
