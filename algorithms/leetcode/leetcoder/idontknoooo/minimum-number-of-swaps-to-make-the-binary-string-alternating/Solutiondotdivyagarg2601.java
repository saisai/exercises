/*
 * https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
 * 
 * https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/discuss/1211069/simplest-explanation-with-java-solution-100-faster
 * 
 * The key to solve this problem is to count number of indexes which contain wrong character. So for string s = 11001, count will be 2 as characters at s[1] and s[2] are wrong. And number of swaps will be count / 2. For example, we can just swap character at index 1 and index 2 to obtain s = 10101.
Things to notice

Solving this problem will be impossible if difference between number of ones and number of zeros will be greater than 1.

If number of ones is greater than number of zeroes then 1 should be the first character of resulting string. Similarly if number of zeroes is greater than number of ones then 0 should be the first character of resulting string.

If number of ones is equal to number of zeroes, we will find minimum number of swaps of both cases:

Case 1 : 1 is the first character.
Case 2 : 0 is the first character.

 */
class Solutiondotdivyagarg2601 {

    public static void main(String[] args){

        Solutiondotdivyagarg2601 S = new Solutiondotdivyagarg2601();
        System.out.println(S.minSwaps("111000"));

    }

    public int minSwaps(String s) {
        
        int ones = 0, zero = 0;
        for(char c : s.toCharArray()) {
            if(c == '1')
            {
                ++ones;
            } else {
                ++zero;
            }
        }

        if(Math.abs(ones-zero) > 1) {
            return -1;
        }

        if(ones > zero) {
            return helper(s, '1');
        } else if(zero > ones) {
            return helper(s, '0');
        }

        return Math.min(helper(s, '1'), helper(s, '0'));
    }

    private int helper(String s, char c) {
        int swaps = 0;
        for(char ch : s.toCharArray()) {
            if(ch != c) {
                ++swaps;
            }
            c ^= 1;
        }
        return swaps / 2;
    }
}