
/*
 * https://leetcode.com/problems/shifting-letters-ii/
 * https://leetcode.com/problems/shifting-letters-ii/discuss/2454324/Prefix-Sum-(Range-Update)-or-O(n)-or-Java-or-6-ms-or-100
 */
class Solution{

    public static void main(String[] args){

        Solution S = new Solution();
        String s = "abc";
        int[][] shifts = {{0,1,0},{1,2,1},{0,2,1}};
        System.out.println(S.shiftingLetters(s, shifts));

    }

    public String shiftingLetters(String s, int[][] shifts){
        char[] ch = s.toCharArray();
        int[] count = new int[s.length()+ 1];

        for(int[] shift: shifts){
            int value = shift[2] == 1 ? 1 : -1;
            count[shift[0]] += value;
            count[shift[1] + 1] -= value; 
        }
        int sum = 0;
        for(int i = 0; i < count.length - 1; i++){
            sum += count[i];
            int newChar = ((ch[i] - 'a') + sum) % 26;
            if(newChar < 0) newChar += 26;
            ch[i] = (char)('a' + newChar);
        }

        return String.valueOf(ch);
    }
}