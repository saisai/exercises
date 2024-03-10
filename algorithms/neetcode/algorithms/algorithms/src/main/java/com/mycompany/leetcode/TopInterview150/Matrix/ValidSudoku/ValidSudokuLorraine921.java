package com.mycompany.leetcode.TopInterview150.Matrix.ValidSudoku;

import java.util.HashSet;

public class ValidSudokuLorraine921 {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < 9; i++) {
            HashSet<Character> rows = new HashSet<Character>();
            HashSet<Character> columns = new HashSet<Character>();
            HashSet<Character> cube = new HashSet<Character>();

            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.' && !rows.add(board[i][j])) {
                    return false;
                }
                if(board[j][i] != '.' && !columns.add(board[j][i])) {
                    return false;
                }
                int RowIndex = 3 * (i / 3);
                int ColIndex = 3 * (i % 3);
                if(board[RowIndex + j /3][ColIndex + j % 3] != '.' && !cube.add(board[RowIndex + j/3][ColIndex + j%3])) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
       char[][] board = {{'5','3','.','.','7','.','.','.','.'}
                        ,{'6','.','.','1','9','5','.','.','.'}
                        ,{'.','9','8','.','.','.','.','6','.'}
                        ,{'8','.','.','.','6','.','.','.','3'}
                        ,{'4','.','.','8','.','3','.','.','1'}
                        ,{'7','.','.','.','2','.','.','.','6'}
                        ,{'.','6','.','.','.','.','2','8','.'}
                        ,{'.','.','.','4','1','9','.','.','5'}
                        ,{'.','.','.','.','8','.','.','7','9'}};
       ValidSudokuLorraine921 obj = new ValidSudokuLorraine921();
       System.out.println(obj.isValidSudoku(board));
    }
}
