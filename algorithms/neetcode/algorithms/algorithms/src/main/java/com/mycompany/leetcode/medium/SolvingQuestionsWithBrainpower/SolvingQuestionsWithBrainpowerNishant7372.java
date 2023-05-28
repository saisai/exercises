package com.mycompany.leetcode.medium.SolvingQuestionsWithBrainpower;

public class SolvingQuestionsWithBrainpowerNishant7372 {
    static long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1];
        for(int i = n - 1; i >= 0; i--) {
            long pick = questions[i][0] + ((i + questions[i][1] + 1) < n ? dp[i + questions[i][1] + 1] : 0);
            long notPick = dp[i+1];
            dp[i] = Math.max(pick, notPick);
        }
        return dp[0];
    }

    public static void main(String[] args) {
        int[][] questions = {{3,2},{4,3},{4,4},{2,5}};
        System.out.println(mostPoints(questions));

    }
}
