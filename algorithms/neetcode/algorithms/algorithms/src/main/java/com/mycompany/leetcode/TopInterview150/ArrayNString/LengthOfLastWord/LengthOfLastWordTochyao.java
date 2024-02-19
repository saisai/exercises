package com.mycompany.leetcode.TopInterview150.ArrayNString.LengthOfLastWord;

public class LengthOfLastWordTochyao {
    public int lengthOfLastWord(String s) {
        int length = 0;

        for(int i = s.length() - 1; i >= 0; i--) {
            if(s.charAt(i) != ' ') {
                length++;
            } else {
                if(length >0) return length;
            }
        }

        return length;
    }

    public static void main(String[] args) {
        LengthOfLastWordTochyao obj = new LengthOfLastWordTochyao();
        String s = "   fly me   to   the moon  ";
        System.out.println(obj.lengthOfLastWord(s));
    }
}
