package com.mycompany.leetcode.blind75.DynamicProgramming.ClimbingStairs;

public class ClimbingStairsSourabhJadhav {
    static int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int[] a= new int[n];
        a[0] = 1;
        a[1] = 2;
        for(int i= 2; i < n; i++) {
            a[i] = a[i-1] + a[i - 2];

        }
        return a[n - 1];
     }

    public static void main(String[] args) {
        System.out.println(climbStairs(3));
    }
}
