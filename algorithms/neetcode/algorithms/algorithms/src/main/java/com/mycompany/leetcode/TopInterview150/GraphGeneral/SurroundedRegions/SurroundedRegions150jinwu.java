package com.mycompany.leetcode.TopInterview150.GraphGeneral.SurroundedRegions;

import java.util.Arrays;

public class SurroundedRegions150jinwu {
    private void DFS(char[][] board, int i, int j) {

        if (i < 0 || i > board.length - 1 || j <0 || j > board[0].length - 1)
            return;

        if(board[i][j] == 'O')
            board[i][j] = '*';
        if (i > 1 && board[i-1][j] == 'O')
            DFS(board, i-1, j);
        if (i < board.length - 2 && board[i+1][j] == 'O')
            DFS(board, i+1, j);
        if (j > 1 && board[i][j-1] == 'O')
            DFS(board, i, j-1);
        if (j < board[i].length - 2 && board[i][j+1] == 'O' )
            DFS(board, i, j+1);
    }

    public void solve(char[][] board) {
        if(board.length == 0 || board[0].length == 0)
            return;
        if(board.length < 2 || board[0].length < 2)
            return;

        int m = board.length, n = board[0].length;

        for(int i = 0; i < m; i++) {
            if(board[i][0] == 'O')
                DFS(board, i, 0);
            if(board[i][n-1] == 'O')
                DFS(board, i, n - 1);
        }


        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O')
                DFS(board, 0, j);
            if (board[m-1][j] == 'O')
                DFS(board, m-1, j);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == '*')
                    board[i][j] = 'O';
            }
        }
    }

    public static void main(String[] args) {
        char[][] board = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
        SurroundedRegions150jinwu obj = new SurroundedRegions150jinwu();

        obj.solve(board);
        System.out.println(Arrays.deepToString(board));
    }
}
