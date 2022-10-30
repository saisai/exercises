
/*
 * 
 * https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/532101/Java-o(n)-one-pass-solution.-Easy-to-understand.
 * https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
 * 
 * Inspired by lee215's solution with some extension to make the solution more easy to understand.

lee 215's solution
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531840/JavaPython-One-Pass

Same idea, we use a state to encode the vowels inforation for prefix string end at index i.

1 State has 5 bits, each bits to indicate if the corresponding vowel have even count or not.

2 When current index have a vowel character, we use bitwise xor to toggle the bit value. state ^= (1 << digit);

3 For the substring between two index have identical state, then all vowels's count are even number.

Eg if from 0 - i, we have even number of 'a', and from 0- j, if we have even number of 'a' again, then the substring between i and j will have even number of 'a' as well. This would be the same if 0 - i and 0 - j both have odd number of 'a'.
Suggested by @multics, we are tracking the value that corresponds to the value of the desired bit to flip. In this way, we can avoid bit shifting.
 * 
 */
import java.util.HashMap;

class Solution {

    HashMap<Character, Integer> vowlToBitIndex = new HashMap<Character, Integer>() {
        {
        put('a', 1);
        put('e', 2);
        put('i', 4);
        put('o', 8);
        put('u', 16);
        }
    };

    public static void main(String[] args){
        Solution S = new Solution();
        String s = "eleetminicoworoep";
        System.out.println(S.findTheLongestSubstring(s));
    }

    public int findTheLongestSubstring(String s) {
        HashMap<Integer, Integer> stateToIndex = new HashMap<>();
        stateToIndex.put(0, -1);
        int state = 0, maxLen = 0;
        for(int i = 0; i < s.length(); ++i) {
            char cur = s.charAt(i);
            if(vowlToBitIndex.containsKey(cur)){
                // flap the digits of the state 1-> 0 or 0 -> 1
                int bitToFlip = vowlToBitIndex.get(cur);
                state ^= bitToFlip;
            }

            stateToIndex.putIfAbsent(state, i);
            maxLen = Math.max(maxLen, i - stateToIndex.get(state));            
        }
        return maxLen;
    }
}