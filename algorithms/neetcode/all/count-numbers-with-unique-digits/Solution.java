/*
 * https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83041/JAVA-DP-O(1)-solution.
 * https://leetcode.com/problems/count-numbers-with-unique-digits/
 * 
 */
class Solution{

    public static void main(String[] args){

        Solution S = new Solution();
        System.out.println(S.countNumbersWithUniqueDigits(2));
    }

    public int countNumbersWithUniqueDigits(int n) {
        if(n == 0) return 1;
        int res = 10;
        int uniqueDigits = 9;
        int availableNumber = 9;
        while(n-- > 1 && availableNumber > 0){
            uniqueDigits = uniqueDigits * availableNumber;
            res += uniqueDigits;
            availableNumber--;
        }
        return res;
    }
}