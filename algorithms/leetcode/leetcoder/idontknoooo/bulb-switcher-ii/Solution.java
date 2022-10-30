/*
 * https://leetcode.com/problems/bulb-switcher-ii
 * https://leetcode.com/problems/bulb-switcher-ii/discuss/107282/Java-O(1)-solution
 */
class Solution {

    public static void main(String[] args){

        Solution S = new Solution();
        int n = 1, presses = 1;
        System.out.println(S.flipLights(n, presses));

    }

    public int flipLights(int n, int m) {
        if(n == 1 && m > 0) {
            return 2;
        } else if (n == 2 && m == 1) {
            return 3;
        } else if((n > 2 && m == 1) || (n == 2 && m > 1)) {
            return 4;
        } else if( n > 2 && m == 2){
            return 7;
        } else if(n > 2 && m > 2) {
            return 8;
        } else {
            return 1;
        }
    }
}