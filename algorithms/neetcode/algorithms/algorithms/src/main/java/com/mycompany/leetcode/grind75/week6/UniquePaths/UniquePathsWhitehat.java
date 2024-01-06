package com.mycompany.leetcode.grind75.week6.UniquePaths;

public class UniquePathsWhitehat {
    public int uniquePaths(int m, int n) {
        if(m == 1 || n == 1)
            return 1;
        m--;
        n--;
        if(m < n) {
            m = m + n;
            n = m - n;
            m = m - n;
        }

        long res = 1;
        int j = 1;
        for(int i = m + 1; i <= m + n; i++, j++) {
            res *= i;
            res /= j;
        }

        return (int) res;
    }

    public static void main(String[] args) {
        int m = 3, n = 7;
        UniquePathsWhitehat obj = new UniquePathsWhitehat();
        System.out.println(obj.uniquePaths(m, n));
    }
}
