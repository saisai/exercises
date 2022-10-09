/*
 * 
 * https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
 * https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/solutions/425110/o-n-time-java-solution-easy-to-understand-with-comments-and-explaination/
 */

import java.util.ArrayList;
import java.util.List;

class Solutiondotmanrajsingh007 {

    public static void main(String[] args) {

        int upper = 2, lower = 1;
        int[] colsum = {1,1,1};

        Solutiondotmanrajsingh007 S = new Solutiondotmanrajsingh007();
        System.out.println(S.reconstructMatrix(upper, lower, colsum));

    }

    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        
        int n = colsum.length;
        int sum0 = 0; // no. of columns with colsum 0
        int sum1 = 0; // no. of columns with colsum 1
        int sum2 = 0; // no. of columns with colsum 2

        for(int i = 0; i < n; i++) {
            if(colsum[i] == 0) sum0 ++;
            else if(colsum[i] == 1) sum1 ++;
            else sum2++;
        }

        int count1 = upper - sum2; // no. of columns with 1 in 1st row and 0 in 2nd row
        int count2 = lower - sum2; // no. of columns with 0 in 1st row and 1 in 2nd row
        
        // check if arrangement is possible or not
        if(count1 < 0 || count2 < 0 || count1 + count2 != sum1) return new ArrayList<>();

        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0; i < 2; i++) ans.add(new ArrayList<>());

        for(int i = 0; i < n; i++){
            if(colsum[i] == 2) {
                ans.get(0).add(1);
                ans.get(1).add(1);
            }else if(colsum[i] == 0){
                ans.get(0).add(0);
                ans.get(1).add(0);
            }
            else{
                if(count1 > 0){
                    count1 --;
                    ans.get(0).add(1);
                    ans.get(1).add(0);
                }
                else{
                    ans.get(0).add(0);
                    ans.get(1).add(1);
                }
            }
        }
        return ans;
    }
}