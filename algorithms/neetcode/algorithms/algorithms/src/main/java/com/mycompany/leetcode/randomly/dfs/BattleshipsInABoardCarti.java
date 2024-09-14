package com.mycompany.leetcode.randomly.dfs;

import com.mycompany.leetcode.grind75.week1.BalancedBinaryTree.BalancedBinaryTreeTusizi;

public class BattleshipsInABoardCarti {
    //recursive helper method for DFS (sink the ships)
    private void DFS(char[][] board, int i, int j) {
        // sink current piece (change to dot)
        board[i][j] = '.';

        // up
        if(i > 0 && board[i-1][j] == 'X') {
            DFS(board, i-1, j);
        }

        // down
        if(i < board.length - 1 && board[i+1][j] == 'X') {
            DFS(board, i + 1, j);
        }

        // left
        if(j > 0 && board[i][j-1] == 'X') {
            DFS(board, i, j - 1);
        }

        // right
        if(j < board[i].length - 1 && board[i][j+1] == 'X') {
            DFS(board, i, j + 1);
        }
    }

    public int countBattleships(char[][] board) {
        // count of our battleships
        int n = 0;

        // iterate thru the board
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                // check if we hit a battleship
                if(board[i][j] == 'X') {
                    // increment count
                    n++;
                    // sink ship
                    DFS(board, i, j);
                }
            }
        }

        return n;
    }

    public static void main(String[] args) {
        char[][] board = {{'X','.','.','X'},{'.','.','.','X'},{'.','.','.','X'}};
        BattleshipsInABoardCarti obj = new BattleshipsInABoardCarti();

        System.out.println(obj.countBattleships(board));

    }
}
