package com.mycompany.leetcode.TopInterview150.Matrix.SetMatrixZeroes;

import java.util.Arrays;

public class SetMatrixZeroesLz2343 {
    public void setZeroes(int[][] matrix) {
        boolean fr = false, fc = false;
        for(int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if(matrix[i][j] == 0) {
                    if(i == 0) fr = true;
                    if(j == 0) fc = true;
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for(int i = 1; i < matrix.length; i++) {
            for(int j = 1; j < matrix[0].length; j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if(fr) {
            for(int j = 0; j < matrix[0].length; j++) {
                matrix[0][j]= 0;
            }
        }

        if(fr) {
            for(int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    public static void main(String[] args) {
        SetMatrixZeroesLz2343 obj = new SetMatrixZeroesLz2343();
        int[][] matrix = {{1,1,1},{1,0,1},{1,1,1}};

        obj.setZeroes(matrix);

        for(int[] data : matrix) {
            System.out.println(Arrays.toString(data));
        }
    }


}
