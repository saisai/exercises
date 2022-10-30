/*
 * https://leetcode.com/problems/split-array-into-fibonacci-sequence/
 * https://leetcode.com/problems/split-array-into-fibonacci-sequence/discuss/133906/Simple-Java-Solution-using-DFS
 */

import java.util.ArrayList;
import java.util.List;

class Solutiondotfaang2022 {

    public static void main(String[] args){

        Solutiondotfaang2022 S = new Solutiondotfaang2022();

        String num = "1101111";
        System.out.println(S.splitIntoFibonacci(num));

    }

    int max = Integer.MAX_VALUE;
    public List<Integer> splitIntoFibonacci(String S) {

        List<Integer> res = new ArrayList<>();
        for(int d = 1; d < S.length(); d++) {
            if(S.charAt(0) == '0' && d > 1) break;
            long num1 = Long.parseLong((S.substring(0,d )));
            if(num1 > max) break;

            // add the first value
            res.add((int)num1);
            for(int i = d; i < S.length(); i++) {
                if(S.charAt(d) == '0' && i > d) break;
                long num2 = Long.parseLong(S.substring(d, i+1 ));
                if (num2 > max) break;

                // add the second value
                res.add((int)num2);
                if(dfs(S, i + 1, (int)num1, (int)num2, res)){
                    return res;
                }

                res.remove(1);                
            }
            res.remove(0);
        }
        return res;
    }

    private  boolean dfs(String s, int k, int num1, int num2, List<Integer> res) {
        if(k == s.length()) {
            if(res.size() > 2) {
                return true;
            } else {
                return false;
            }
        }

        for(int i = k; i < s.length(); i++) {
            if(s.charAt(k) == '0' && i > k) break;
            long tmp = Long.parseLong(s.substring(k, i + 1));
            if(tmp > max) return false;

            // value equals the sum of last two values
            if(tmp == num1+num2) {
                res.add((int)tmp);
                if(dfs(s, i+1, (int)num2, (int)tmp, res)) return true;
                res.remove(res.size() - 1);
            } else if(tmp > num1+num2) return false;
        }
        return false;
    }

}