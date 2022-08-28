/*
 * https://leetcode.com/problems/sum-game/
 * https://leetcode.com/problems/sum-game/discuss/1329069/Java-Greedy-O(n)-solution-with-detailed-explaination-covering-every-case
 * 
 */
class Solution {

    public static void main(String[] args){

        Solution S = new Solution();
        String num = "5023";
        System.out.println(S.sumGame(num));

    }

    public boolean sumGame(String num) {
        int diff = 0;
        int left = 0;
        int right = 0;
        for(int i =0; i < num.length() / 2; i++){
            if(num.charAt(i) == '?') {
                left++;
            } else {
                diff += num.charAt(i) - '0';
            }
        }

        for(int i= num.length() / 2; i < num.length(); i++){
            if(num.charAt(i) == '?') {
                right++;
            } else {
                diff -= num.charAt(i) - '0';
            }
        }

        // situation 2
        if((right + left) % 2 == 1) return true;
        // Situation 1 and 3
        if(left == right) {
            return diff != 0;
        }

        int round = (left - right) / 2;
        // situation a
        if(diff * round >= 0) return true;
        return Math.abs(diff) != Math.abs(round * 9);
    }
}