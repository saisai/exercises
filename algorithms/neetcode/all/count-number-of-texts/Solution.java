/*
 * https://leetcode.com/problems/count-number-of-texts/
 * https://leetcode.com/problems/count-number-of-texts/discuss/2021176/clean-java
 */

import java.util.HashSet;
import java.util.Set;

class Solution {

    String[] map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    int MOD = (int)1e9 + 7;
    public static void main(String[] args){
        String pressedKeys = "22233";
        Solution S = new Solution();
        System.out.println(S.countTexts(pressedKeys));
    }

    public int countTexts(String pressedKeys) {
        Set<Integer> set = new HashSet<>();
        for(int i=2; i <= 9; i++) {
            int num = 0;
            String str = map[i];
            for(int j = 0; j < str.length(); j++){
                num = num * 10 + i;
                set.add(num);
            }            
        }

        int N = pressedKeys.length();
        long[] dp = new long[N];
        dp[0] = 1;
        // decode ways
        for(int i= 1; i < N; i++) {
            int num = 0;
            for(int j = i; j >= Math.max(0, i -4); j--){
                num = num * 10 + (pressedKeys.charAt(j) - '0');
                if(set.contains(num)){
                    if(j == 0) dp[i] = (dp[i] + 1) % MOD;
                    else dp[i] = (dp[i] + dp[j - 1]) % MOD;
                }
            }
        }
        return (int) dp[N-1];

    }
}